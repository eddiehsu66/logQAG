import openai
from src.config.redisKit import redisInit
from src.config.configLoad import load_config

openai.api_base, openai.api_key = load_config('OPENAI_API_BASE'), load_config('OPENAI_API_KEY')


def infer_llm(instruction, exemplars, query, model='gpt-3.5-turbo-0125', temperature=0.0, max_tokens=2048, logger=None,
              cached=False):
    messages = [
        # {"role": "system", "content": roleSystem},
        {"role": "user", "content": instruction},
        # {"role": "assistant", "content": roleAssistant},
    ]
    if exemplars is not None:
        for i, exemplar in enumerate(exemplars):
            messages.append({"role": "user", "content": exemplar['query']})
            messages.append(
                {"role": "assistant", "content": exemplar['answer']})
    if query is not None:
        messages.append({"role": "user", "content": query})

    client = redisInit()

    if cached:
        response = client.get(instruction)
        if response is not None:
            return response

    retry_times = 0
    while retry_times < 3:
        try:
            answers = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                stream=False,
            )
            res = [response["message"]["content"] for response in answers["choices"] if
                   response['finish_reason'] != 'length'][0]
            if cached:
                client.set(instruction, res)
            return res
        except Exception as e:
            if logger is not None:
                logger.info("Exception : {}".format(e))
            else:
                print("Exception :", e)
            if "list index out of range" in str(e):
                break
            retry_times += 1
    if exemplars is not None and len(exemplars) > 0:
        if exemplars[0]['query'] != 'Log message: `try to connected to host: 172.16.254.1, finished.`' \
                or exemplars[0]['answer'] != 'Log template: `try to connected to host: {ip_address}, finished.`':
            return infer_llm(instruction, exemplars, query,cached=cached)
        if logger is not None:
            logger.error(f"Failed to get response from OpenAI after {retry_times} retries.")
        else:
            print(f"Failed to get response from OpenAI after {retry_times} retries.")
    return "Failed to get response from OpenAI after {} retries.".format(retry_times)
if __name__ == '__main__':
    text = ""

    # 由gpt生成日志解析模版，输出模版放在提示词的最后面
    prompt1 = "I gave a friend an instruction and five inputs. " \
              "The friend read the instruction and wrote an output for every one of the inputs. " \
              f"Here are the input-outputpairs: \n{text}" \
              f"Please output my instruction to the friend, only instruction, without any superfluous output"

    # 由gpt生成日志解析模版，输出模版放在提示词的中间
    prompt2 = "I instructed my friend to <>. " \
              "The friend read the instruction and wrote an output for every one of the inputs. " \
              f"Here are the input-outputpairs: \n{text}" \
              f"Please output my instruction to the friend, only instruction, without any superfluous output"
    # 由gpt生成日志解析模版，输出模版放在提示词的中间
    prompt3 = "Professor Smith was given the following instruction:<>" \
              f"Here are the Professor's responses: \n{text} " \
              f"Please output the instruction, only instruction, without any superfluous output"

    prompts = [prompt1, prompt2, prompt3]

    for prompt in prompts:
        response = infer_llm(prompt, None, None)
        print(response)
        print("gpt生成的提示词:", response)
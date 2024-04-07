import matplotlib.pyplot as plt
import matplotlib

# 设置matplotlib的字体为支持中文的字体，例如：微软雅黑
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['font.size'] = 10
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False


def draw_plot_with_keys(data):
    # [ga, fga, pa]
    max_pa = []
    max_ga = []
    max_fga = []
    for i in data:
        max_ga_value = 0
        max_fga_value = 0
        max_pa_value = 0
        for j in i.values():
            max_ga_value = max(max_ga_value, j[0])
            max_fga_value = max(max_fga_value, j[1])
            max_pa_value = max(max_pa_value, j[2])
        max_ga.append(max_ga_value)
        max_fga.append(max_fga_value)
        max_pa.append(max_pa_value)

    x_indexes = range(len(data))
    plt.figure(figsize=(12, 8))
    plt.plot(x_indexes, max_pa, color='red',label='pa')
    plt.plot(x_indexes, max_ga, color='green',label='ga')
    plt.plot(x_indexes, max_fga, color='blue',label='fga')
    plt.title('autoPrompt')
    plt.xlabel('迭代次数')
    plt.ylabel('准确率')
    plt.legend()
    plt.grid(True)
    path = 'C:/code/src/python/autoQAG/result/result.png'
    plt.savefig(path, dpi=300)


if __name__ == '__main__':
    data = [
        {'Replace the placeholders in the given inputs with <*>.': 0.2, '<>': 0.12,
         'Replace the placeholders in the given outputs with the corresponding values from the inputs.': 0.14,
         'Anonymize all sensitive information in the given inputs.': 0.14,
         'Mask any sensitive information before providing output.': 0.08,
         ' Fill in the blanks in the provided results with the matching values from the inputs.': 0.1,
         ' Replace the placeholders in the displayed outcomes with the corresponding input values.': 0.12,
         ' What is the meaning of the prompt?': 0.04, ' Can you explain the prompt in more detail?': 0.02,
         ' Replace the placeholders in the given inputs with <*>': 0.16,
         ' Fill in the blanks in the provided inputs with <*>': 0.1,
         ' Remove all identifying information from the provided inputs.': 0.16,
         ' Ensure that all sensitive data in the given inputs is anonymized.': 0.14,
         ' Mask any confidential data before displaying the results.': 0.1,
         ' Conceal sensitive information before presenting the output.': 0.1},
        {'Replace the placeholders in the given inputs with <*>.': 0.22,
         ' Replace the placeholders in the given inputs with <*>': 0.38,
         ' Remove all identifying information from the provided inputs.': 0.22,
         'Replace the placeholders in the given outputs with the corresponding values from the inputs.': 0.2,
         'Anonymize all sensitive information in the given inputs.': 0.2,
         ' Fill in the blanks in the provided results with the matching data from the inputs.': 0.1,
         ' Replace the placeholders in the displayed outcomes with the relevant values from the inputs.': 0.22,
         ' Remove all personal details from the given inputs.': 0.2,
         ' Erase any identifying information from the provided inputs.': 0.2,
         ' Fill in the blanks in the provided inputs with <*>': 0.14,
         ' Remove any identifying information from the provided inputs.': 0.24,
         ' Ensure that all sensitive data is anonymized in the given inputs.': 0.22,
         ' Substitute the placeholders in the provided inputs with <*>': 0.18},
        {' Replace the placeholders in the given inputs with <*>': 0.44,
         ' Remove any identifying information from the provided inputs.': 0.14,
         'Replace the placeholders in the given inputs with <*>.': 0.2,
         ' Remove all identifying information from the provided inputs.': 0.16,
         ' Replace the placeholders in the displayed outcomes with the relevant values from the inputs.': 0.16,
         ' Remove any identifying information from the inputs.': 0.18,
         ' Ensure that all identifying information is removed from the provided inputs.': 0.16,
         ' Fill in the blanks in the provided inputs with <*>': 0.2,
         ' Fill in the blanks in the shown results with the appropriate data from the inputs.': 0.1,
         ' Replace the placeholders in the outcomes with the relevant values provided.': 0.14,
         ' Remove all personal details from the given inputs.': 0.14,
         ' Erase any identifying information from the provided inputs.': 0.16},
        {' Replace the placeholders in the given inputs with <*>': 0.28,
         'Replace the placeholders in the given inputs with <*>.': 0.12,
         ' Fill in the blanks in the provided inputs with <*>': 0.34,
         ' Remove any identifying information from the inputs.': 0.26,
         ' Remove all identifying information from the provided inputs.': 0.14,
         ' Remove all personal details from the given inputs.': 0.12,
         ' Erase any identifying information from the provided inputs.': 0.14,
         ' Ensure that all identifying information is removed from the inputs.': 0.12,
         ' Replace the placeholders in the provided inputs with <*>': 0.12},
        {' Fill in the blanks in the provided inputs with <*>': 0.38,
         ' Replace the placeholders in the given inputs with <*>': 0.28,
         ' Remove any identifying information from the inputs.': 0.16,
         ' Remove all identifying information from the provided inputs.': 0.12,
         ' Erase any identifying information from the provided inputs.': 0.14,
         ' Remove any personal details from the given inputs.': 0.28,
         ' Erase all identifying information from the provided inputs.': 0.12,
         ' Remove any personal details from the inputs.': 0.16,
         ' Remove any identifiable information from the inputs.': 0.16,
         ' Delete all identifying information from the provided inputs.': 0.1},
        {' Fill in the blanks in the provided inputs with <*>': 0.36,
         ' Replace the placeholders in the given inputs with <*>': 0.3,
         ' Remove any personal details from the given inputs.': 0.16,
         ' Remove any identifying information from the inputs.': 0.54,
         ' Remove any personal details from the inputs.': 0.12,
         ' Ensure that all identifying information is removed from the inputs.': 0.16,
         ' Remove all personal details from the inputs.': 0.18,
         ' Replace the placeholders in the provided inputs with <*>': 0.18,
         ' Remove all personal information from the provided inputs.': 0.16,
         ' Erase any personal details from the given inputs.': 0.16},
        {' Remove any identifying information from the inputs.': 0.38,
         ' Fill in the blanks in the provided inputs with <*>': 0.4,
         ' Replace the placeholders in the given inputs with <*>': 0.5,
         ' Remove all personal details from the inputs.': 0.12,
         ' Replace the placeholders in the provided inputs with <*>': 0.32,
         ' Eliminate all personal details from the inputs.': 0.12,
         ' Ensure that all identifying information is removed from the inputs.': 0.14},
        {' Replace the placeholders in the given inputs with <*>': 0.2,
         ' Fill in the blanks in the provided inputs with <*>': 0.24,
         ' Remove any identifying information from the inputs.': 0.24,
         ' Replace the placeholders in the provided inputs with <*>': 0.2,
         ' Ensure that all identifying information is removed from the inputs.': 0.22,
         ' Fill in the blanks in the given inputs with <*>': 0.08,
         ' Remove all identifying information from the inputs.': 0.1,
         ' Make sure to delete any identifying details from the inputs.': 0.12,
         ' Complete the missing parts in the given inputs with <*>': 0.06},
        {' Fill in the blanks in the provided inputs with <*>': 0.3,
         ' Remove any identifying information from the inputs.': 0.18,
         ' Ensure that all identifying information is removed from the inputs.': 0.1,
         ' Replace the placeholders in the given inputs with <*>': 0.42,
         ' Replace the placeholders in the provided inputs with <*>': 0.48,
         ' Remove all identifying information from the inputs.': 0.1,
         ' Make sure to delete any identifying details from the inputs.': 0.1,
         ' Eliminate all personal details from the inputs.': 0.12},
        {' Replace the placeholders in the provided inputs with <*>': 0.26,
         ' Replace the placeholders in the given inputs with <*>': 0.28,
         ' Fill in the blanks in the provided inputs with <*>': 0.28,
         ' Remove any identifying information from the inputs.': 0.16,
         ' Eliminate all personal details from the inputs.': 0.14,
         ' Remove all personal information from the inputs.': 0.12,
         ' Erase any personal details from the inputs.': 0.14, ' Remove any personal details from the inputs.': 0.12,
         ' Remove any identifiable information from the inputs.': 0.16,
         ' Fill in the blanks in the given inputs with <*>': 0.02},
        {' Replace the placeholders in the given inputs with <*>': 0.36,
         ' Fill in the blanks in the provided inputs with <*>': 0.36,
         ' Replace the placeholders in the provided inputs with <*>': 0.36,
         ' Remove any identifying information from the inputs.': 0.32,
         ' Remove any identifiable information from the inputs.': 0.16,
         ' Fill in the blanks in the given inputs with <*>': 0.22,
         ' Remove any personal details from the inputs.': 0.12, ' Remove any identifiable data from the inputs.': 0.14,
         ' Ensure that all identifying information is removed from the inputs.': 0.12},
        {' Replace the placeholders in the given inputs with <*>': 0.3,
         ' Fill in the blanks in the provided inputs with <*>': 0.34,
         ' Replace the placeholders in the provided inputs with <*>': 0.5,
         ' Remove any identifying information from the inputs.': 0.16,
         ' Fill in the blanks in the given inputs with <*>': 0.26, ' Remove any personal details from the inputs.': 0.2,
         ' Remove all identifying information from the inputs.': 0.18,
         ' Complete the inputs by filling in the blanks with <*>': 0.16},
        {' Replace the placeholders in the provided inputs with <*>': 0.32,
         ' Fill in the blanks in the provided inputs with <*>': 0.48,
         ' Replace the placeholders in the given inputs with <*>': 0.28,
         ' Fill in the blanks in the given inputs with <*>': 0.26,
         ' Remove any personal details from the inputs.': 0.16,
         ' Remove any identifying information from the inputs.': 0.16,
         ' Remove all personal details from the inputs.': 0.12,
         ' Complete the inputs by inserting <*> in the blanks.': 0.1},
        {' Fill in the blanks in the provided inputs with <*>': 0.56,
         ' Replace the placeholders in the provided inputs with <*>': 0.46,
         ' Replace the placeholders in the given inputs with <*>': 0.36,
         ' Fill in the blanks in the given inputs with <*>': 0.32,
         ' Remove any personal details from the inputs.': 0.16,
         ' Remove any identifying information from the inputs.': 0.2,
         ' Ensure that all personal details are removed from the inputs.': 0.16,
         ' Complete the inputs by inserting <*> in the blanks.': 0.12},
        {' Fill in the blanks in the provided inputs with <*>': 0.44,
         ' Replace the placeholders in the provided inputs with <*>': 0.22,
         ' Replace the placeholders in the given inputs with <*>': 0.24,
         ' Fill in the blanks in the given inputs with <*>': 0.28,
         ' Remove any identifying information from the inputs.': 0.14,
         ' Replace the missing values in the provided inputs with <*>': 0.06,
         ' Remove any personal details from the inputs.': 0.12,
         ' Remove all identifying information from the inputs.': 0.16},
        {' Fill in the blanks in the provided inputs with <*>': 0.7,
         ' Fill in the blanks in the given inputs with <*>': 0.32,
         ' Replace the placeholders in the given inputs with <*>': 0.62,
         ' Replace the placeholders in the provided inputs with <*>': 0.46,
         ' Remove all identifying information from the inputs.': 0.2,
         ' Complete the inputs by filling in the blanks with <*>': 0.16,
         ' Remove all personal details from the inputs.': 0.18,
         ' Erase any identifying information from the inputs.': 0.2},
        {' Fill in the blanks in the provided inputs with <*>': 0.4,
         ' Replace the placeholders in the given inputs with <*>': 0.28,
         ' Replace the placeholders in the provided inputs with <*>': 0.46,
         ' Fill in the blanks in the given inputs with <*>': 0.28,
         ' Remove all identifying information from the inputs.': 0.14,
         ' Remove all personal details from the inputs.': 0.16,
         ' Erase any identifying information from the inputs.': 0.12},
        {' Replace the placeholders in the provided inputs with <*>': 0.4,
         ' Fill in the blanks in the provided inputs with <*>': 0.62,
         ' Replace the placeholders in the given inputs with <*>': 0.62,
         ' Fill in the blanks in the given inputs with <*>': 0.28,
         ' Remove all personal details from the inputs.': 0.16,
         ' Complete the inputs by filling in the blanks with <*>': 0.14,
         ' Remove any identifying information from the inputs.': 0.16,
         ' Eliminate all personal details from the inputs.': 0.16},
        {' Fill in the blanks in the provided inputs with <*>': 0.26,
         ' Replace the placeholders in the given inputs with <*>': 0.38,
         ' Replace the placeholders in the provided inputs with <*>': 0.42,
         ' Fill in the blanks in the given inputs with <*>': 0.16,
         ' Remove all personal details from the inputs.': 0.14,
         ' Complete the inputs by filling in the blanks with <*>': 0.12,
         ' Remove all identifying information from the inputs.': 0.16,
         ' Erase any personal details from the inputs.': 0.14},
        {' Replace the placeholders in the provided inputs with <*>': 0.2,
         ' Replace the placeholders in the given inputs with <*>': 0.22,
         ' Fill in the blanks in the provided inputs with <*>': 0.18,
         ' Fill in the blanks in the given inputs with <*>': 0.1,
         ' Remove all identifying information from the inputs.': 0.1,
         ' Remove all personal details from the inputs.': 0.1,
         ' Erase any identifying information from the inputs.': 0.08,
         ' Replace the missing values in the given inputs with <*>': 0.06,
         ' Complete the inputs by filling in the blanks with <*>': 0.04},
    ]
    draw_plot_with_keys(data)
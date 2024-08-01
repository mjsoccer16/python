import pandas as pd
import code_1 

file_path = r"C:\Users\heman\Desktop\Python Project\input.xlsx"
df = pd.read_excel(file_path)
df_values = df.values[1:].tolist()
urls = [item[1] for item in df_values]
# print(urls)


# for i in urls:
s = code_1.gather(urls[0])
print(s[0])


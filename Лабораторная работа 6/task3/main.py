OUTPUT_FILE = "output.csv"
def to_csv_file(filename, headers, rows, delimiter=None, new_line=None):
    if delimiter==None:
        delimiter=','
    if new_line==None:
        new_line="\n"
    with open(filename, 'w') as f:
        for word in headers:
            if word!=headers[-1]:          #понимаю, что нехорошо, что каждый раз условие проверяется
                f.write(word+delimiter)    #но побыстрее ничего не придумал
            else:                          #собственно, цель состоит в том, чтобы лишний раз delimiter не проставить
                f.write(word)
        f.write(new_line)
        for list_ in rows:
            for value in list_:
                if value!=list_[-1]:
                    f.write(value+delimiter)
                else:
                    f.write(value)
            f.write(new_line)

# TODO реализовать функцию to_csv_file


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

# TODO вызвать функцию to_csv_file и записать данные в файл
filename="output.csv"
to_csv_file(filename, headers_list, data)

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")

class Markdown:
    COMMAND = ['plain', 'bold', 'italic', 'header', 'link',
               'inline-code', 'new-line', 'ordered-list', 'unordered-list']

    def __init__(self, text=''):
        self.text = text

    def get_help(self) -> None:
        print(f'''Available formatters: {self.COMMAND}
        Special commands: !help !done''')

    def get_header(self) -> str:
        while True:
            try:
                level = int(input('Level: '))
                if 0 < level < 7:
                    input_text = str(input('Text: '))
                    header = level * '#'
                    text_formatter = header + ' ' + input_text + '\n'
                    self.text += text_formatter
                    return self.text
                else:
                    print('The level should be within the range of 1 to 6')
            except ValueError:
                print('Wrong format level')

    def get_bold(self) -> str:
        input_text = str(input('Text: '))
        bold_text = '**' + input_text + '**'
        self.text += bold_text
        return self.text

    def get_italic(self) -> str:
        input_text = str(input('Text: '))
        italic_text = '*' + input_text + '*'
        self.text += italic_text
        return self.text

    def get_plain(self) -> str:
        text = str(input('Text: '))
        self.text += text
        return self.text

    def get_inline_code(self) -> str:
        input_text = str(input('Text: '))
        inline_code = '`' + input_text + '`'
        self.text += inline_code
        return self.text

    def get_new_line(self) -> str:
        self.text += '\n'
        return self.text

    def get_link(self) -> str:
        label = '[' + str(input('Label: ')) + ']'
        url = '(' + str(input('URL: ')) + ')'
        self.text += label + url
        return self.text

    def get_list(self, order=True) -> str:
        while True:
            rows_list = {}
            try:
                rows = int(input('Number of rows'))
                if rows <= 0:
                    print('The number of rows should be greater than zero')
                else:
                    for i in range(1, rows + 1):
                        row_element = input(f'Row #{i}: ')
                        rows_list[str(i)] = row_element

                    for row, element in rows_list.items():
                        if not order:
                            row = '*'
                            text_list = f'{row} {element}' + '\n'
                        else:
                            text_list = f'{row}. {element}' + '\n'
                        self.text += text_list
                    return self.text

            except ValueError:
                print('Enter integer number')

    def save(self) -> None:
        with open('output.md', 'w') as f:
            f.write(self.text)
            print('file saved!')

    def menu(self) -> None:
        while True:
            answer = input('Choose a formatter: ').lower()
            if answer == '!done':
                self.save()
                break
            elif answer == '!help':
                self.get_help()
            elif answer not in self.COMMAND:
                print('Unknown formatting type or command')
            elif answer == 'ordered-list':
                print(self.get_list())
            elif answer == 'unordered-list':
                print(self.get_list(False))
            else:
                answer = answer.replace('-', '_')
                call_method = 'get_' + answer
                getattr(self, call_method)()
                print(self.text)


test_1 = Markdown()
test_1.menu()


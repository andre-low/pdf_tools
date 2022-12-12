from PyPDF2 import PdfReader, PdfWriter

INPUT_FILE_ODD = str(input(
    'Enter the input file for odd pages (default = odd.pdf): ') or 'odd.pdf')
INPUT_FILE_EVEN = str(input(
    'Enter the input file for odd pages (default = even.pdf): ') or 'even.pdf')
PAGES_PER_DOCUMENT = int(input(
    'Pages per document (i.e. split every n pages) (default = 2): ') or '2')

with open(INPUT_FILE_ODD, 'rb') as input_odd_read_file:
    input_odd = PdfReader(input_odd_read_file)
    total_pages_odd = len(input_odd.pages)

    with open(INPUT_FILE_EVEN, 'rb') as input_even_read_file:
        input_even = PdfReader(input_even_read_file)
        total_pages_even = len(input_even.pages)

        alternate_mix = PdfWriter()

        for page in range(total_pages_odd):
            alternate_mix.add_page(input_odd.pages[page])

            if total_pages_odd == total_pages_even:
                alternate_mix.add_page(
                    input_even.pages[total_pages_odd - page - 1])
            elif total_pages_odd == total_pages_even + 1:
                alternate_mix.add_page(
                    input_even.pages[total_pages_odd - page - 2])
            else:
                print('Error')

        for document in range(-((total_pages_odd + total_pages_even) // -PAGES_PER_DOCUMENT)):
            output = PdfWriter()

            if (PAGES_PER_DOCUMENT % 2) == 0:
                for page in range(PAGES_PER_DOCUMENT):
                    output.add_page(
                        alternate_mix.pages[document * PAGES_PER_DOCUMENT + page])
            else:
                try:
                    for page in range(PAGES_PER_DOCUMENT):
                        output.add_page(
                            alternate_mix.pages[document * (PAGES_PER_DOCUMENT + 1) + page])
                except:
                    break

            OUTPUT_NAME = 'output_' + str(document + 1) + '.pdf'

            with open(OUTPUT_NAME, 'wb') as write_file:
                output.write(write_file)
                print('Created ' + OUTPUT_NAME)

def display_segments(number, segments):
    digit_segments = [
        'abcdef',  # 0
        'bc',      # 1
        'abged',   # 2
        'abcdg',   # 3
        'bcfg',    # 4
        'acdfg',   # 5
        'acdefg',  # 6
        'abc',     # 7
        'abcdefg', # 8
        'abcdfg'   # 9
    ]

    binary_truth_table = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001'
    }

    seven_segment_display = {
        '0': '1111110',
        '1': '0110000',
        '2': '1101101',
        '3': '1111001',
        '4': '0110011',
        '5': '1011011',
        '6': '1011111',
        '7': '1110000',
        '8': '1111111',
        '9': '1111011'
    }

    for row in segments:
        displayed_line = ''
        for digit in str(number):
            for segment_char in row:
                if segment_char.isalpha() and segment_char.lower() in digit_segments[int(digit)]:
                    displayed_line += segment_char
                else:
                    displayed_line += ' '
        print(displayed_line)

    print()

    print("Binary:")
    for digit in str(number):
        print(f'{binary_truth_table[digit]} ', end='')

    print()
    print()
    
    print("Seven segments:")
    for digit in str(number):
        print(f'{seven_segment_display[digit]} ', end='')

number = int(input("Masukkan Angka yang Ingin Anda Tampilkan: "))

segments = [
    '  AAAAA  ',
    ' F     B ',
    ' F     B ',
    ' F     B ',
    '  GGGGG  ',
    ' E     C ',
    ' E     C ',
    ' E     C ',
    '  DDDDD  '
]

display_segments(number, segments)

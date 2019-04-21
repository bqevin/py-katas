def char_count(haystack, needle, hit):
    haystack = list(haystack)
    new_length = len(haystack)

    if new_length == 0:
        return

    if haystack[0].lower() == needle.lower():
        hit += 1
    char_count(haystack[1:new_length], needle, hit)

    if len(haystack[1:new_length]) == 0:
        print('Count for letter  \'' + needle + '\' is: ' + str(hit))


char_count('Today is Easter', 'e', 0)

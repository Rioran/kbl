# KBL file specification

KeyBoard Layout file is intended for KBL project for easy import and export of user defined layouts.

### Structure

KBL is a usual text file, separated by newlines.

- first row reserved for layout name
- second row reserved for optional layout description, leave empty if not needed
- all other rows represent a translation of us keys into alternative keys
    - every key map row must be at least 2 symbols long
    - final map will take first row symbol as us key
    - final map will take last row symbol as alternative key

### Example

This is a valid content for "russian.kbl" file:

```txt
RU
Classic Russian keyboard for Windows
a - ф
b - и
```
# PNG-TO-PDF

> convert pngs into pdfs faster using pillow

Requirements:
`pillow` | 
```pip install pillow```


How does the script work?
- Script asks for the root folder where all the pngs are. It searches for all the nested folders/directories for pngs.
- It stores all found pngs in a list
- It splits the list into 2.
- Creates 2 processes, sends one list to first process, second list to second process.
- All pdfs are generated in the same directory where pngs and with the same file name.

If you're using this code, mention my name or link to this github repo. Everything is free to use. You can also choose not to mention my name or repo link. Happy Coding!

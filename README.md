# PyQT Column Sorting Example

This demonstrates a problem where a PyQt table view is not sorting properly on anything but the first column.

## Running

First install the dependencies:
```bash
pip install -r requirements.txt
```

Then run the program:
```bash
python gui.py
```

This should pop up a GUI with a table. If you click on the header for the first column, you'll see that it sorts the data lexically, alternating between ascending and descending. This is the expected behavior. Howver, if you do the same on the second column, you get no sorting at all. This is the problem I'd like to solve: why doesn't the second column sort like the first?

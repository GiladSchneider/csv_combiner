# CSV Combiner
Hi PMG Team!
This is my submission for the csv-combiner programming challenge. To start, populate the 'fixtures' file with as many csv files as you would like. To quickly get started, you can run:
```
$ python3 generate_fixtures.py
```

Then, to combine your fixtures, run the following:
```
$ python3 src/csv_combiner.py ./fixtures/<filename 1> ./fixtures/<filename 2>  ./fixtures/<filename 3> ... ./fixtures/<filename N> > combined.csv 
```
For example:
```
python3 src/csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv  ./fixtures/accessories.csv > combined.csv
```

To unit test the program, run:
```
pytest
```


## Orginization
The main code is located in the 'csv_combiner.py' file in the src directory.
You can find the unit tests in the 'test_csv_combiner.py' file.

I look forward to writing more code alongside you!

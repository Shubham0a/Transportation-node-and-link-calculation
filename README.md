# Transportation 


## node-and-link-calculation

## minimum distance between each node calculation
![min-distance](https://user-images.githubusercontent.com/75657176/209528984-976f2c42-0268-4931-836c-1836d679b04f.png)
## Installation
Use the package manager [pip](https://pypi.org/project/osm2gmns/) to install osm file converter to csv file.
```bash
pip install osm2gmns
```
special thanks to: _**openstreetmap**_
and
_**Jiawei Lu, Xuesong (Simon) Zhou**_
and
_**some other scources which helped me**_
## Usage
## Download map.osm file from **openstreet** [link*](https://www.openstreetmap.org/)
### Use method as follows:-
> 1. Open the website of openstreet from the [link*](https://www.openstreetmap.org/).


> 2. Go to export ans select the location.

> 3. export the osm file. 

> 4. run the scource code with map.osm *_Note: Both should be in same directory_*

> 5. run transportation.exe file (_i was unable to upload due to big size so you can download from [here](https://drive.google.com/drive/folders/1n1E5jdavlOMDy0e7kOIWQePagbK3KJZL?usp=sharing) or you may mail me to get it on *shubhamiit30@gmail.com*_)
*note: please download the folder named transport and add map.osm file in dist folder and then run transportation.exe in dist folder.*

> 6. distance.txt file will be created which contains minimum distance corresponding to each node.

```python
import os
import csv

import osm2gmns as og

.
.
.
.

with open('link.csv') as csv_file:
.
.

```

## Contact Me

Feel free to contact me:-

[JOIN ME](https://shubham-0a.github.io/portfolio/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

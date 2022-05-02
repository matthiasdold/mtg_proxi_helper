# MTG Proxi Helper
Trying a bit with proxi printing it seems like the best way of generating playable proxies, is to cut the proxie to exactly match the inner card frame and glue it to an original (keeping its black border).

This script helps you to create a proxie sheet with 9 cards, cropped to the right size and aligned, so that one cut between adjacent cards is enough.

## Usage
Simply collect the links of the 9 proxies you need from [scryfall](https://scryfall.com/) and past them line by line into the `cards.txt`
```bash
cat cards.txt                                                                                                                                                                via v3.10.4
   https://scryfall.com/card/mh2/439/scalding-tarn
   https://scryfall.com/card/mh2/439/scalding-tarn
   https://scryfall.com/card/mh2/439/scalding-tarn
   https://scryfall.com/card/mh2/440/verdant-catacombs
   https://scryfall.com/card/mh2/440/verdant-catacombs
   https://scryfall.com/card/mh2/440/verdant-catacombs
   https://scryfall.com/card/mh2/437/marsh-flats
   https://scryfall.com/card/mh2/437/marsh-flats
   https://scryfall.com/card/mh2/437/marsh-flats
```

then run the script, which will create proxi_set.pdf
```python
python build_proxi.py
```


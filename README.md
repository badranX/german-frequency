Morphology extractor from different sources. For example, in English, "playing" and "played" might be found seperated in a dataset. This code adresses this issue by taking morphology into account.

## Example:
The file 5000.txt (in the 'data' folder) contains top 5000 German words ranked by frequency based on German movie subtitles. Each item on the list is a one word of a group of related words by morphologies. 

- The german data was generated via [LuminosoInsight](https://github.com/LuminosoInsight/wordfreq) and [german-morph-dictionaries](https://github.com/DuyguA/german-morph-dictionaries).

[   :: Data](#Data)
[   :: Evaluation](#Evaluation)
[   :: Development Languages](#Development)
[   :: Surprise Languages](#Surprise)
[   :: Results](#Results)


# Data

This repository contains the Development and Surprise languages for SIGMORPHON 2020 Task 0 (Typologically Diverse Morphlogical Inflection).  
All data files are in canonicalized format (see tags.yaml for possible tags): tags start with POS, and features follow lexicographic order. 
Tags follow [UniMorph schema](https://unimorph.github.io/) that was slightly extended with a few new tags (such as ``1+INCL''; due to new languages). 
We additionally `provide' WALS features [here](https://wals.info/download) for those who choose to use them (allowed for both constrained and unconstrained submissions).


# Evaluation

Update: Please use `compute_acc_single.py` to evaluate your systems.

```
python compute_acc_single.py --gold gld.tst --sysout pred.tst

```

The official evaluation script `evaluate.py` lives in this directory.
You may run the evaluation script as shown in the example below.

```
python3 evaluate.py --hyp lang.hyp --ref lang.dev

accuracy:	67.30
levenshtein:	0.93
```





# Languages
## Development
| Family | Genus | Code | Language | Source of Data | Annotator | 
|----    |---    |---   |---       |----            |---        |
|Austronesian   |Barito   |mlg(plt)   |[Malagasy](https://en.wikipedia.org/wiki/Malagasy_language)      |Modern Malagasy Verbs. CreateSpace Independent Publishing Platform  |Jennifer White| 
|    |Greater Central Philippine   |ceb   |[Cebuano](https://en.wikipedia.org/wiki/Cebuano_language)  |----            | Ran Zmigrod      |
|    |Greater Central Philippine  |hil   |[Hiligaynon](https://en.wikipedia.org/wiki/Hiligaynon_language) |Hiligaynon Language: 101 Hiligaynon Verbs by Anj Santos | Ran Zmigrod      |
|    |Greater Central Philippine  |tgl   |[Tagalog](https://en.wikipedia.org/wiki/Tagalog_language)     | [Center for Southeast Asian Studies, NIU](http://www.seasite.niu.edu/tagalog/tagalog_verbs.htm)           | Jennifer White    |
|    |Oceanic  |mao(mri)  |[Maori](https://en.wikipedia.org/wiki/M%C4%81ori_language)      | [maoridictionary.co.nz](https://maoridictionary.co.nz/)          | Jennifer White       |
|Indo-European  | Germanic   |ang   |[Old English](https://en.wikipedia.org/wiki/Old_English) |UniMorph|        |
|    |Germanic   |dan   |[Danish](https://en.wikipedia.org/wiki/Danish_language) | UniMorph |       |
|    |Germanic    |deu   |[German](https://en.wikipedia.org/wiki/German_language) | UniMorph            |       |
|    |Germanic    |eng   |[English](https://en.wikipedia.org/wiki/English_language) | UniMorph            |     |
|    |Germanic    |frr   |[North Frisian](https://en.wikipedia.org/wiki/North_Frisian_language)     | UniMorph           |     |
|    |Germanic    |gmh   |[Middle High German](https://en.wikipedia.org/wiki/Middle_High_German)       | UniMorph            |  |
|    |Germanic  |isl   |[Icelandic](https://en.wikipedia.org/wiki/Icelandic_language)|UniMorph          |     |
|    |Germanic    |nld   |[Dutch](https://en.wikipedia.org/wiki/Dutch_language)|UniMorph           |      |
|    |Germanic     |nob   |[Norwegian Bokmål](https://en.wikipedia.org/wiki/Bokm%C3%A5l)      | UniMorph            |       |
|    |Germanic     |swe   |[Swedish](https://en.wikipedia.org/wiki/Swedish_language)      | UniMorph           |      |
|Niger-Congo |Bantoid   |kon(kng)   |[Kongo](https://en.wikipedia.org/wiki/Kongo_language)|Modern Kongo Verbs. CreateSpace Independent Publishing Platform |Jennifer White|
|    |Bantoid    |lin   |[Lingala](https://en.wikipedia.org/wiki/Lingala) |----            |---        |
|    |Bantoid   |lug   |[Luganda](https://en.wikipedia.org/wiki/Luganda)     |Namono, Mirembe. (2018). Luganda language: 101 Luganda verbs. CreateSpace Independent Publishing Platform. |Edoardo Ponti|
|    |Bantoid    |nya   |[Chewa](https://en.wikipedia.org/wiki/Chewa_language)  |102 Swahili Verbs. CreateSpace Independent Publishing Platform  | Ryan Cotterell   |
|    |Bantoid |sot   |[Sotho](https://en.wikipedia.org/wiki/Sotho_language) |----            |---        |
|    |Bantoid    |swa(swh)   |[Swahili](https://en.wikipedia.org/wiki/Swahili_language) |----            |Jennifer White|
|    |Bantoid    |zul   |[Zulu](https://en.wikipedia.org/wiki/Zulu_language)       |----            |---        |
|    |Kwa   |aka   |[Akan](https://en.wikipedia.org/wiki/Akan_language) |Imbeah, Paa Kwesi. (2012). 102 Akan verbs. CreateSpace Independent Publishing Platform. |Tiago Pimentel |
|    |Kwa   |gaa   |[Gã](https://en.wikipedia.org/wiki/Ga_language)       |102 Ga verbs. CreateSpace Independent Publishing Platform.|Tiago Pimentel  |
|Oto-Manguean    |Amuzgoan  |azg   |[San Pedro Amuzgos Amuzgo](https://en.wikipedia.org/wiki/Amuzgo_language)       | Surrey Morphology Group          |  Antonis Anastasopoulos   |
|    |Chichimec  |pei   |[Chichimeca-Jonaz](https://en.wikipedia.org/wiki/Chichimeca_Jonaz_language)      | Surrey Morphology Group       | Antonis Anastasopoulos |
|    |Chinantecan   |cpa  |[Tlatepuzco Chinantec](https://en.wikipedia.org/wiki/Palantla_Chinantec)       | Surrey Morphology Group            |  Antonis Anastasopoulos      |
|    |Mixtecan   |xty   |[Yoloxóchitl Mixtec](https://en.wikipedia.org/wiki/Yolox%C3%B3chitl_Mixtec)       | Surrey Morphology Group            |  Antonis Anastasopoulos      |
|    |Otomian   |ote   |[Mezquital Otomi](https://en.wikipedia.org/wiki/Northwestern_Otomi)  | Surrey Morphology Group           |  Antonis Anastasopoulos      |
|    |Otomian  |otm   |[Sierra Otomi](https://en.wikipedia.org/wiki/Sierra_Otomi)  | Surrey Morphology Group     | Antonis Anastasopoulos       |
|    |Zapotecan    |cly   |[Eastern Highland Chatino](https://en.wikipedia.org/wiki/Highland_Chatino)| Cruz, Hilaria; Anastasopoulos, Antonis and Stump, Gregory. 2020 (to appear at LREC). A Resource for Studying Chatino Verbal Morphology    |  Antonis Anastasopoulos     |
|    |Zapotecan |ctp   |[Yaitepec Chatino](https://en.wikipedia.org/wiki/Chatino_language)   | Surrey Morphology Group       | Antonis Anastasopoulos      |
|    |Zapotecan  |czn   |[Zenzontepec Chatino](https://en.wikipedia.org/wiki/Zenzontepec_Chatino)  | Surrey Morphology Group          | Antonis Anastasopoulos    |
|    |Zapotecan    |zpv   |[Chichicapan Zapotec](https://en.wikipedia.org/wiki/Chichic%C3%A1pam_Zapotec)      | Surrey Morphology Group          |  Antonis Anastasopoulos      |
|Uralic    |Finnic    |est   |[Estonian](https://en.wikipedia.org/wiki/Estonian_language)    | UniMorph          |        |
|    |Finnic    |fin   |[Finnish](https://en.wikipedia.org/wiki/Finnish_language)     | UniMorph           |        |
|    |Finnic    |izh   |[Ingrian](https://en.wikipedia.org/wiki/Ingrian_language)       | UniMorph            |        |
|    |Finnic   |krl   |[Karelian](https://en.wikipedia.org/wiki/Karelian_language)      |[VepKar](http://dictorpus.krc.karelia.ru/en) | Natalia Krizhanovskaya|
|    |Finnic  |liv   |[Livonian](https://en.wikipedia.org/wiki/Livonian_language)       |----            |---        |
|    |Finnic   |vep   |[Veps](https://en.wikipedia.org/wiki/Veps_language)    |[VepKar](http://dictorpus.krc.karelia.ru/en) | Natalia Krizhanovskaya |
|    |Finnic   |vot   |[Votic](https://en.wikipedia.org/wiki/Votic_language)  | UniMorph |   |
|    |Mari   |mhr   |[Meadow Mari](https://en.wikipedia.org/wiki/Meadow_Mari_language)    |[Tim Arkhangelskij](http://meadow-mari.web-corpora.net/index_en.html)  |Liz Salesky and Ekaterina Vylomova  |
|    |Mordvin    |mdf   |[Moksha](https://en.wikipedia.org/wiki/Moksha_language)       |[Tim Arkhangelskij](http://moksha.web-corpora.net/index_en.html)|Liz Salesky and Ekaterina Vylomova |
|    |Mordvin    |myv   |[Erzya](https://en.wikipedia.org/wiki/Erzya_language)      |[Tim Arkhangelskij](http://erzya.web-corpora.net/index_en.html)|Liz Salesky and Ekaterina Vylomova |
|    |Saami   |sme   |[Northern Sami](https://en.wikipedia.org/wiki/Northern_Sami_language)       | UniMorph    |         |

## Surprise

| Family | Genus | Code | Language | Source of Data | Annotator | 
|----|---|---|---|----|---|
| Afro-Asiatic | Semitic | mlt |[Maltese](https://en.wikipedia.org/wiki/Maltese_language) | UniMorph |    |
|| Lowland East Cushitic | orm | [Oromo](https://en.wikipedia.org/wiki/Oromo_language) |    | Irene Nikkarinen |
| | Semitic | syc | [Syriac](https://en.wikipedia.org/wiki/Syriac_language) | UniMorph |    |
| Algic | Algonquian| cre | [Cree](https://en.wikipedia.org/wiki/Cree_language)| Hunter, James. (1923). A lecture on the grammatical construction of the Cree language and Paradigms of the Cree Verb, with its various conjugations, moods, tenses, inflections, &c. The Society for Promoting Christian Knowledge. London. (Original work published 1875). | Eleanor Chodroff|
| Altaic | Tungusic | evn | [Evenki](https://en.wikipedia.org/wiki/Evenki_language) | Elena Klyachko | Elena Klyachko |
|  | Turkic | aze(azb) | [Azerbaijani](https://en.wikipedia.org/wiki/Azerbaijani_language) | UniMorph |    |
|  | Turkic | bak | [Bashkir](https://en.wikipedia.org/wiki/Bashkir_language)|    |    |
|  | Turkic | crh | [Crimean Tatar](https://en.wikipedia.org/wiki/Crimean_Tatar_language) |    |    |
|  | Turkic | kaz | [Kazakh](https://en.wikipedia.org/wiki/Kazakh_language) |1) Nabiyev, Temir. (2015). Kazakh language: 101 Kazakh verbs. Preceptor Language Guides. Great Britain. 2) Turkicum. (2019). The Kazakh verbs: Review guide. Turkicum. Great Britain.  | Eleanor Chodroff |
|  | Turkic  | kir | [Kyrgyz](https://en.wikipedia.org/wiki/Kyrgyz_language) | Aytnatova, Alima. (2016). Kyrgyz language: 100 Kyrgyz verbs fully conjugated in all tenses. CreateSpace Independent Publishing Platform. Middletown, DE. | Eleanor Chodroff |
|  | Turkic | kjh | [Khakas](https://en.wikipedia.org/wiki/Khakas_language) |    |    |
|  | Turkic | tuk | [Turkmen](https://en.wikipedia.org/wiki/Turkmen_language) | 1)Abdulin, Murat. (2016). Turkmen verbs: 100 Turkmen verbs conjugated in all tenses. CreateSpace Independent Publishing Platform. 2)Peace Corps (n.d.). 501 Turkmen verbs. US Embassy in Turkmenistan. | Eleanor Chodroff |
|    | Turkic | uig | [Uyghur](https://en.wikipedia.org/wiki/Uyghur_language) | Kadeer, Alim. Uyghur language: 94 Uyghur verbs in common tenses. CreateSpace Independent Publishing Platform. |Eleanor Chodroff |
|    | Turkic | uzb | [Uzbek](https://en.wikipedia.org/wiki/Uzbek_language) | 1) Abdullaev, Daniyar. (2016). Uzbek language: 100 Uzbek verbs conjugated in common tenses. CreateSpace Independent Publishing Platform. 2) Turkicum. (2019). The Uzbek verbs: Review guide. Turkicum. Great Britain.  | Eleanor Chodroff|
| Dravidian | Southern Dravidian | kan | [Kannada](https://en.wikipedia.org/wiki/Kannada) | UniMorph |    |
|        |South-Central Dravidian| tel | [Telugu](https://en.wikipedia.org/wiki/Telugu_language) | UniMorph |    |
| Indo-European  | Indic | ben | [Bengali](https://en.wikipedia.org/wiki/Bengali_language) | UniMorph |    |
|    | Indic | hin | [Hindi](https://en.wikipedia.org/wiki/Hindi) |    |    | 
|    | Indic | san | [Sanskrit](https://en.wikipedia.org/wiki/Sanskrit_language) | UniMorph |    |
|    | Indic | urd | [Urdu](https://en.wikipedia.org/wiki/Urdu_language)| UniMorph |    |
|    | Iranian | fas(pes) | [Persian](https://en.wikipedia.org/wiki/Persian_language) | UniMorph |    |
|    | Iranian | pus(pst) | [Pashto](https://en.wikipedia.org/wiki/Pashto_language) | UniMorph |    |
|    | Iranian | tgk | [Tajik](https://en.wikipedia.org/wiki/Tajik_language)|    | Eleanor Chodroff|
|    | Romance | ast | [Asturian](https://en.wikipedia.org/wiki/Asturian_language) | UniMorph |    |
|    | Romance | cat | [Catalan](https://en.wikipedia.org/wiki/Catalan_language) | UniMorph |    |
|    | Romance | frm | [Middle French](https://en.wikipedia.org/wiki/Middle_French) | UniMorph |    |
|    | Romance | fur | [Friulian](https://en.wikipedia.org/wiki/Friulian_language)| UniMorph |    |
|    | Romance | glg | [Galician](https://en.wikipedia.org/wiki/Galician_language) | UniMorph |    |
|    | Romance | lld | [Ladin](https://en.wikipedia.org/wiki/Ladin_language) | UniMorph |    |
|    | Romance | vec | [Venetian](https://en.wikipedia.org/wiki/Venetian_language) | UniMorph |    |
|    | Romance | xno | [Anglo-Norman](https://en.wikipedia.org/wiki/Anglo-Norman_language) |    |    |
|   -| West Germanic | gml | [Middle Low German](https://en.wikipedia.org/wiki/Middle_Low_German) | UniMorph |    |
|    | West Germanic | gsw |[Swiss German](https://en.wikipedia.org/wiki/Swiss_German) | Egli-Wilde, Renate. Züritüütsch verstaa, Züritüütsch rede.    | Ryan Cotterell |
|    | North Germanic | nno | [Norwegian Nynorsk](https://en.wikipedia.org/wiki/Nynorsk) | UniMorph |    |
|    |    |    |    |    |    |
| Niger-Congo | Bantoid | sna | [Shona](https://en.wikipedia.org/wiki/Shona_language) |    | Rowan Hall Maudslay |
|    |    |    |    |    |    |
|Sino-Tibetan | Bodic | bod | [Tibetan](https://en.wikipedia.org/wiki/Standard_Tibetan) | [Di et al., 2019](https://www.aclweb.org/anthology/U19-1005.pdf) | Qianji Di |
| Siouan | Core Siouan | dak | [Dakota](https://en.wikipedia.org/wiki/Dakota_language) | LaFontaine, Harlan & McKay, Neil. (2004). 550 Dakota verbs. Minnesota Historical Society. St. Paul, MN. | Eleanor Chodroff |
| Songhay | Songhay | dje |[Zarma](https://en.wikipedia.org/wiki/Zarma_language)|    | Ran Zmigrod |
| Southern Daly | Murrinh-Patha | mwf | [Murrinh-Patha](https://en.wikipedia.org/wiki/Murrinh-patha_language) | John Mansfield | John Mansfield |
| Uralic | Permic | kpv | [Komi-Zyrian](https://en.wikipedia.org/wiki/Komi_language) | [Tim Arkhangelskij](https://github.com/timarkh/uniparser-grammar-komi-zyrian) | Liz Salesky and Ekaterina Vylomova |
|    | Finnic | lud | [Ludic](https://en.wikipedia.org/wiki/Ludian_language)| [VepKar](http://dictorpus.krc.karelia.ru/en) | Natalia Krizhanovskaya |
|    | Finnic | olo | [Livvi](https://en.wikipedia.org/wiki/Livvi_language) | [VepKar](http://dictorpus.krc.karelia.ru/en) | Natalia Krizhanovskaya |
|    | Permic | udm | [Udmurt](https://en.wikipedia.org/wiki/Udmurt_language) | [Tim Arkhangelskij](https://github.com/timarkh/uniparser-grammar-udm/) |  Liz Salesky and Ekaterina Vylomova |
|    | Finnic | vro | [Võro](https://en.wikipedia.org/wiki/V%C3%B5ro_language) | Vitalij Chernyavskij | Ekaterina Vylomova |
| Uto-Aztecan | Tepiman | ood | [O'odham](https://en.wikipedia.org/wiki/O%27odham) | Zepeda, Ofelia. (2003). A Tohono O'odham grammar. University of Arizona Press. (Original work published 1983). | Eleanor Chodroff |


# Results

The shared task received 23 systems from 10 teams. The results on test data are available [HERE](https://docs.google.com/spreadsheets/d/1ODFRnHuwN-mvGtzXA1sNdCi-jNqZjiE-i9jRxZCK0kg/edit?usp=sharing) 


# Instaloader: download onder andere foto's van Instagram:

Installeren kan met:
```bash
pip install instaloader
```
Dan kun je bijvoorbeeld alle afbeeldingen downloaden van een profiel naar een mapje, bijvoorbeeld van `waterschappen`. Het kan zijn dat je moet inloggen of dat dat betere afbeeldingen oplevert, dat kan met `--login <<insta_handle>>`.
```
instaloader waterschappen [--login <<mijn_insta_handle>>]
```
Het zou ook mogelijk moeten zijn foto's onder een bepaalde hashtag op te vragen met bijvoorbeeld:
```
instaloader "#water" [--login <<mijn_insta_handle>>]
```
Deze werkt helaas niet op dit moment... Zie https://github.com/instaloader/instaloader/issues/1588.

Zie ook [de docs van Instaloader](https://instaloader.github.io/) voor onder andere meer mogelijkheden.


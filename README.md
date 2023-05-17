# Save your Subs

Do you actually like your sub? Go save them.  
I ofc talk about subreddits. Back up the data.   
No Backup, No Mercy.

## Usage

> Depending on your os it could be `python3`, `pyhon` or something completely different.

### Installation

```shell
# go to the desired installation path

# downloading the repository
git clone https://github.com/Lewd-Heal-Girl/save-your-subs.git

# installing the dependencies 
cd save_your_subs
python3 -m pip install -r requirements.txt
```

### Run

```shell
python3 -m save_your_subs r/HealSluts
```

```
usage: save_your_subs [-h] [-e] sub

positional arguments:
  sub           your little sub (r/your_sub)

options:
  -h, --help    show this help message and exit
  -e, --export  Exports the downloaded backup, to a csv file.
```

## Functionalities

- [x] Download the Metadata from every reddit Post on a subreddit.
- [x] Downloading all Imgur Pictures from the reddit Posts.
- [x] Downloading all pictures from all posts
- [x] Support for all image hoster like for example catbox (this can only be done with single images though)
- [ ] Download videos from Redgifs.
- [ ] Download gallerie from imgchest (?) *never heard of that one though.*
- [x] Export to csv file and export the images in a clean way

## Export

If you export the data, it reads the api responses, and dumps them to a json file, while assigning every post a numerical id. This is used to get cleaner file names for the images.

|subreddit        |title                                                                              |artist             |flair          |url                                                                                                         |id  |images|reddit_id |
|-----------------|-----------------------------------------------------------------------------------|-------------------|---------------|------------------------------------------------------------------------------------------------------------|----|------|----------|
|ImaginaryMonsters|Ra by Christoph Peters                                                             |One_Giant_Nostril  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/ulnz6c/ra_by_christoph_peters/                          |0000|1     |t3_ulnz6c |
|ImaginaryMonsters|Saul Goodman                                                                       |blackbrush1618     |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/wowz6r/saul_goodman/                                    |0001|1     |t3_wowz6r |
|ImaginaryMonsters|Junior &amp; Senior ^.^                                                            |LadyAbraxus        |               |https://www.reddit.com/r/ImaginaryMonsters/comments/uri380/junior_senior/                                   |0002|1     |t3_uri380 |
|ImaginaryMonsters|this idea came from a drunken night with my friends XD                             |Gambacurta         |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/z7u167/this_idea_came_from_a_drunken_night_with_my/     |0003|1     |t3_z7u167 |
|ImaginaryMonsters|Three Rangers                                                                      |Number1GamerJohn   |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/12a4m0y/three_rangers/                                  |0004|1     |t3_12a4m0y|
|ImaginaryMonsters|Judgement by Tomasz Ryger                                                          |standyourground10  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/onzrd3/judgement_by_tomasz_ryger/                       |0005|1     |t3_onzrd3 |
|ImaginaryMonsters|Swamp Troll Bounty by Simon Hetu                                                   |One_Giant_Nostril  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/137g634/swamp_troll_bounty_by_simon_hetu/               |0006|1     |t3_137g634|
|ImaginaryMonsters|M27 S.A.M.E Type "Shortfin": Kaijune 2022 day 27 - Artillery                       |Fluffysbeans       |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/vmfe2n/m27_same_type_shortfin_kaijune_2022_day_27/      |0007|1     |t3_vmfe2n |
|ImaginaryMonsters|I was told my recent painting may belong here                                      |SympathyAfter4336  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/weznmr/i_was_told_my_recent_painting_may_belong_here/   |0008|1     |t3_weznmr |
|ImaginaryMonsters|Smurf Sighting by Nate Hallinan                                                    |One_Giant_Nostril  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/v0wqr0/smurf_sighting_by_nate_hallinan/                 |0009|1     |t3_v0wqr0 |
|ImaginaryMonsters|"Homo Mycelium" by Me                                                              |Randicore          |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/x391d8/homo_mycelium_by_me/                             |0010|0     |t3_x391d8 |
|ImaginaryMonsters|Dark art.                                                                          |art_zdesiseitsas   |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/zewzas/dark_art/                                        |0011|1     |t3_zewzas |
|ImaginaryMonsters|Falling Devil [Chainsaw Man] by 疾風✦Hayate                                          |Zewen_Senpai       |               |https://www.reddit.com/r/ImaginaryMonsters/comments/124xvd8/falling_devil_chainsaw_man_by_疾風hayate/         |0012|1     |t3_124xvd8|
|ImaginaryMonsters|Captured Pilot by Christian Johnson                                                |One_Giant_Nostril  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/ths9jv/captured_pilot_by_christian_johnson/             |0013|1     |t3_ths9jv |
|ImaginaryMonsters|"Devout Colossus" by me                                                            |Crondisimo         |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/127zvtz/devout_colossus_by_me/                          |0014|1     |t3_127zvtz|
|ImaginaryMonsters|Golem Powered by an Imprisoned Angel - Concept for Devil May Cry enemy by Dan Baker|natezomby          |Incorrect title|https://www.reddit.com/r/ImaginaryMonsters/comments/5glfv2/golem_powered_by_an_imprisoned_angel_concept_for/|0015|1     |t3_5glfv2 |
|ImaginaryMonsters|KAIJU By Cho Yonghee                                                               |maybeharu          |               |https://www.reddit.com/r/ImaginaryMonsters/comments/xovbx1/kaiju_by_cho_yonghee/                            |0016|1     |t3_xovbx1 |
|ImaginaryMonsters|stare into the abyss.........                                                      |After_Meringue_8619|               |https://www.reddit.com/r/ImaginaryMonsters/comments/12s2ftb/stare_into_the_abyss/                           |0017|1     |t3_12s2ftb|
|ImaginaryMonsters|Prisoner                                                                           |30xap              |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/10p15qk/prisoner/                                       |0018|1     |t3_10p15qk|
|ImaginaryMonsters|Vampire Boss by Egor Grishin                                                       |One_Giant_Nostril  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/8ryk0b/vampire_boss_by_egor_grishin/                    |0019|1     |t3_8ryk0b |
|ImaginaryMonsters|Supa Buzi Slugtopuzzi - by Ameshin                                                 |Ameshin            |Self-submission|https://www.reddit.com/r/ImaginaryMonsters/comments/vr2vqg/supa_buzi_slugtopuzzi_by_ameshin/                |0020|0     |t3_vr2vqg |
|ImaginaryMonsters|Somebody Toucha My Spaghet! by Peter Sandeman                                      |One_Giant_Nostril  |               |https://www.reddit.com/r/ImaginaryMonsters/comments/fgv5mp/somebody_toucha_my_spaghet_by_peter_sandeman/    |0021|1     |t3_fgv5mp |


# Imgur

## Detect Galleries and Single Posts

- Example for Single: `https://i.imgur.com/DeYIbo6.png"`
- Example for Gallery: `https://imgur.com/a/zpCKPPs`

Thus, if there is a `.{format}`, then the picture is a single picture. If not it is a gallery.

If the picture is only one, it can be called directly, else following stepts need to be taken:

## Donwloading a Gallerie

This gets the data of a gallery

`GET: https://api.imgur.com/post/v1/albums/{imgur_id}?include=media`

## Response from a gallery:

```json
{
	"id": "zpCKPPs",
	"title": "Cass' Relaxation",
	"media": [
		{
			"id": "Tq7kG4f",
			"account_id": 0,
			"mime_type": "image/png",
			"type": "image",
			"name": "Cass and Steph (Text) 1..png",
			"basename": "",
			"url": "https://i.imgur.com/Tq7kG4f.png",
			"ext": "png",
			"width": 1902,
			"height": 1055,
			"size": 817919,
			"metadata": {
				"title": "",
				"description": "Part 1",
				"is_animated": false,
				"is_looping": false,
				"duration": 0,
				"has_sound": false
			},
			"created_at": "2022-12-31T21:19:53Z",
			"updated_at": null
		},
        ...
	],
	"display": []
}
```

# Takeaways

> REDGIFS HOSTS IMAGES????????

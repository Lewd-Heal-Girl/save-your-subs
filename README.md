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
positional arguments:
  sub         your little sub (r/your_sub)

options:
  -h, --help  show this help message and exit
```

## Functionalities

- [x] Download the Metadata from every reddit Post on a subreddit.
- [x] Downloading all Imgur Pictures from the reddit Posts.
- [x] Downloading all pictures from all posts
- [ ] Support for all image hoster like for example catbox (this can only be done with single images though)

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
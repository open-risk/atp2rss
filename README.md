# atp2rss
A small toolkit to help convert AT Protocol and ActivityPub subscription lists to RSS. 

## Description

The toolkit consists of two Python scripts that convert follow lists from Bluesky and Mastodon respectively into OPML files that can be imported into any RSS reader. This way you can keep track of posts from accounts that post infrequently and might get lost in the default "timeline" interface of these platforms.

![Screenshot](Screenshot.png)

## How to use

* Clone or fork this repository in your computer
* Export your follow lists from Bluesky and/or the Mastodon instance you have an account on. The scripts work independently, generating two separate OPML files. 
  * The Bluesky export filename is _repo.car_
  * The Mastodon export filename is _following_accounts.csv_
* Run **python3 ap.py** inside the cloned repo. This creates the OPML file _mastodon_feeds.opml_
* Run **python3 at.py**. This creates the OPML file _bluesky_feeds.opml_. NB: it may take a while for a long list as it needs to resolve the names of feeds from an online service.
* 4. Import the feeds into your favorite reader(s).


## Dependencies

To parse the AtProto export (CAR file) we need the atproto library (also needed for resolving did's).

## Troubleshooting

* On bluesky long lists may hit rate limits
* On mastodon various accounts may actually be federated from instances that do not provide RSS feeds
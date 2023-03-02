# About

This is inspired by [https://github.com/StevenBlack/hosts](https://github.com/StevenBlack/hosts). You should definitely check him out!
This is my personal block list, where I add sketchy hosts I stumble upon. You are welcome to use the list as you like.

- Last updated: 2023-03-02 19:15:42
- Number of entries: 391

I'm distributing a "verbose" list with line comments, a minified version without comments and a compressed version with several entries in one line. It seems like windows could run into an performance issue if you use the first two versions, whereas my PiHole seems happy about the "bloated" verbose one.

# Contribute

## Missing something
Feel free to open up an [issue](https://github.com/Cuupa/hosts/issues/new?template=add-host.md&title=Add+new+host) with the hostname and the category (like 'malware' or 'scam') you think fit.

## Your site is blocked
Please open an [issue](https://github.com/Cuupa/hosts/issues/new?template=unblock-host.md&title=Unblock+host), if you think a site is mistakenly blocked. Please provide the url(s) and please add a statement why your site should be unblocked.

# Usage

This list works with a [PiHole](https://pi-hole.net) as well [Adguard-Home](https://adguard.com/de/adguard-home/overview.html) 

On Android you can use [AdAway](https://f-droid.org/packages/org.adaway/). Unfortunatelly the app is only provided by f-droid, because it violates the Google Play Store terms and conditions.

You can either use the [combined list](https://raw.githubusercontent.com/Cuupa/hosts/main/hosts) or select what you want to block using the seperate lists provided unter [data](https://github.com/Cuupa/hosts/tree/main/data/)

## PiHole
- Login at your PiHole admin interface
- Navigate to "Adlists"
- Copy the URL to the hostfile into the "Address" inputfield:

 [https://raw.githubusercontent.com/Cuupa/hosts/main/hosts](https://raw.githubusercontent.com/Cuupa/hosts/main/hosts),
 [https://raw.githubusercontent.com/Cuupa/hosts/main/hosts_minfied](https://raw.githubusercontent.com/Cuupa/hosts/main/hosts_minified) or [https://raw.githubusercontent.com/Cuupa/hosts/main/hosts_compressed](https://raw.githubusercontent.com/Cuupa/hosts/main/hosts_compressed)
- OPTIONAL: Provide a description
- Click "Add"
- Update your gravity list (webinterface or via 'pihole -g')

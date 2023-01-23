# About

This is inspired by [https://github.com/StevenBlack/hosts](https://github.com/StevenBlack/hosts). You should definitely check him out!

This is my personal block list, where I add sketchy hosts I stumble upon. You are welcome to use the list as you like

In the future I plan to take my entries and add them to the corresponding block list of SteveBlack.

# Contribute

## Missing something
Feel free to open up an issue with the hostname and the category (like advare or scam) you think fit.

## Your site is blocked
Please open an issue if you think your site is mistakenly blocked. Please provide the url of your site and a statement why your site should be unblocked.

# Usage

This list works well with a [PiHole](https://pi-hole.net) as well as [AdAway](https://f-droid.org/packages/org.adaway/). The later is unfortunatelly only provided by f-droid because it violates the Google Play Store terms and conditions.

## PiHole
- Login at your PiHole admin interface
- Navigate to "Adlists"
- Copy the URL to the hostfile into the "Address" inputfield:

 [https://github.com/Cuupa/hosts/hosts](https://github.com/Cuupa/hosts/hosts) or [https://github.com/Cuupa/hosts/hosts_compressed](https://github.com/Cuupa/hosts/hosts_compressed)
- OPTIONAL: Provide a description
- Click "Add"
- Update your gravity list (webinterface or via 'pihole -g')
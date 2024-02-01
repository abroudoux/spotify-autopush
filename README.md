# spotify-autopush

![Repo Size](https://img.shields.io/github/repo-size/abroudoux/spotify-autopush)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.12-blue)

## 💻・About

Spotify-Autopush is a program to display on your Github account your last album played so you can show the world your great musical tastes (no one cares)

## 🎯・Setup

In construction...

## 📚・Ressources

- [Spotify API](https://developer.spotify.com/documentation/web-api)
- [Github API](https://docs.github.com/en/rest/users/users?apiVersion=2022-11-28)

## 🧑‍🤝‍🧑・Contributing

To use Auto-Push in development, follow these steps:

1. Fork the project.

2. Install poetry.

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

3. Create a branch with [conventionnal name](https://tilburgsciencehub.com/building-blocks/collaborate-and-share-your-work/use-github/naming-git-branches/).

   - fix: `bugfix/the-bug-fixed`
   - features: `feature/the-amazing-feature`
   - test: `test/the-famous-test`
   - hotfix `hotfix/oh-my-god-bro`
   - wip `wip/the-work-name-in-progress`

4. Configure your environment variables in `.env`.

```
SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=
SPOTIFY_REDIRECT_URI=
GITHUB_USERNAME=
GITHUB_PERSONAL_ACCESS_TOKEN=
```

## 🎯・Roadmap

- [ ] Push the last album played on my portfolio
- [ ] Create a CLI

## 📑・Licence

This project is under MIT license. For more information, please see the file [LICENSE](./LICENSE).

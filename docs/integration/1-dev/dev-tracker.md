---

kanban-plugin: basic

---

## Packages

- [ ] [[Tailwind]]<br><br>ADR: #PENDING <br><br>Depends: #Prettier, #BrowserList<br><br>Install: #Npm
- [ ] [[Prettier-plugin-tailwindcss]]<br><br>`npm install -D prettier prettier-plugin-tailwindcss`<br><br>Depdendant:
  #Tailwinds ^09ajzj
- [ ] [[Setting  Browserlist]]<br><br>`"browserslist": [  <br>">0.3%, defaults and supports es6-module",  <br>"maintained node versions"  <br>]`<br><br>
  Query [Browserslist](https://browsersl.ist/#q=%3E0.3%25%2C+defaults%2C+supports+es6-module%2C+maintained+node+versions)<br><br>
  #Depends
- [ ] Autofixer
- [ ] PostCSS
- [ ] 
  Modern-Normalise<br>[sindresorhus/modern-normalize: 🐒 Normalize browsers' default style (github.com)](https://github.com/sindresorhus/modern-normalize)<br>
  Builds On

## Configured

## In Use

## Deployed

%% kanban:settings

```
{"kanban-plugin":"basic","new-note-template":"docs/templates/Dev {{title}}.md","new-note-folder":"docs/integration/dev","show-checkboxes":true,"hide-tags-in-title":false}
```

%%
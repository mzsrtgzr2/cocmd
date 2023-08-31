"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[9671],{3905:(e,t,r)=>{r.d(t,{Zo:()=>p,kt:()=>f});var n=r(7294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function a(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function l(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?a(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function i(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},a=Object.keys(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(n=0;n<a.length;n++)r=a[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var s=n.createContext({}),c=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):l(l({},t),e)),r},p=function(e){var t=c(e.components);return n.createElement(s.Provider,{value:t},e.children)},u="mdxType",d={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,a=e.originalType,s=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),u=c(r),m=o,f=u["".concat(s,".").concat(m)]||u[m]||d[m]||a;return r?n.createElement(f,l(l({ref:t},p),{},{components:r})):n.createElement(f,l({ref:t},p))}));function f(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=r.length,l=new Array(a);l[0]=m;var i={};for(var s in t)hasOwnProperty.call(t,s)&&(i[s]=t[s]);i.originalType=e,i[u]="string"==typeof e?e:o,l[1]=i;for(var c=2;c<a;c++)l[c]=r[c];return n.createElement.apply(null,l)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},9881:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>l,default:()=>d,frontMatter:()=>a,metadata:()=>i,toc:()=>c});var n=r(7462),o=(r(7294),r(3905));const a={sidebar_position:1},l="Getting Started",i={unversionedId:"intro",id:"intro",title:"Getting Started",description:"Cocmd is an open source tool for Developers to add aliases and scripts to their Bash terminal commands (or any other Shell - zsh, fish etc).",source:"@site/docs/intro.md",sourceDirName:".",slug:"/intro",permalink:"/cocmd/docs/intro",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/intro.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",next:{title:"Technologies",permalink:"/cocmd/docs/category/technologies"}},s={},c=[{value:"1. Install",id:"1-install",level:3},{value:"2. Setup",id:"2-setup",level:3},{value:"3. Add Tech Packs",id:"3-add-tech-packs",level:3}],p={toc:c},u="wrapper";function d(e){let{components:t,...r}=e;return(0,o.kt)(u,(0,n.Z)({},p,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"getting-started"},"Getting Started"),(0,o.kt)("p",null,"Cocmd is an open source tool for Developers to add aliases and scripts to their Bash terminal commands (or any other Shell - zsh, fish etc)."),(0,o.kt)("p",null,"For example, lets say you have a lot of ",(0,o.kt)("inlineCode",{parentName:"p"},"git")," commands you type in during the day. Use CoCMD to easily add ",(0,o.kt)("inlineCode",{parentName:"p"},"git")," related scripts, shortcuts and automations to your terminal. "),(0,o.kt)("h3",{id:"1-install"},"1. Install"),(0,o.kt)("p",null,"First, please install cocmd with pip or poetry:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"pip install cocmd\n")),(0,o.kt)("h3",{id:"2-setup"},"2. Setup"),(0,o.kt)("p",null,"Second, we need some information for the first setup:"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"cocmd setup\n")),(0,o.kt)("p",null,"You will get several questions to make CoCMD work for you:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"what is your shell")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"this is important because we setup aliases and PATH in the rc file ")),(0,o.kt)("ol",{start:2},(0,o.kt)("li",{parentName:"ol"},"scan depth (default is ",(0,o.kt)("em",{parentName:"li"},"1"),")")),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"for each source, how deep to scan for ",(0,o.kt)("inlineCode",{parentName:"li"},"cocmd.yaml")," file.")),(0,o.kt)("h3",{id:"3-add-tech-packs"},"3. Add Tech Packs"),(0,o.kt)("p",null,"Add your favorite technologies"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-bash"},"cocmd add tech <tech>\n")),(0,o.kt)("p",null,"You will get a list of possible technologies to add to the cmd."))}d.isMDXComponent=!0}}]);
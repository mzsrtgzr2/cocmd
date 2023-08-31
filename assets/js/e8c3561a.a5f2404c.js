"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[4111],{3905:(e,t,n)=>{n.d(t,{Zo:()=>u,kt:()=>k});var r=n(7294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function l(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function i(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var s=r.createContext({}),c=function(e){var t=r.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):l(l({},t),e)),n},u=function(e){var t=c(e.components);return r.createElement(s.Provider,{value:t},e.children)},p="mdxType",b={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},d=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,u=i(e,["components","mdxType","originalType","parentName"]),p=c(n),d=a,k=p["".concat(s,".").concat(d)]||p[d]||b[d]||o;return n?r.createElement(k,l(l({ref:t},u),{},{components:n})):r.createElement(k,l({ref:t},u))}));function k(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,l=new Array(o);l[0]=d;var i={};for(var s in t)hasOwnProperty.call(t,s)&&(i[s]=t[s]);i.originalType=e,i[p]="string"==typeof e?e:a,l[1]=i;for(var c=2;c<o;c++)l[c]=n[c];return r.createElement.apply(null,l)}return r.createElement.apply(null,n)}d.displayName="MDXCreateElement"},3565:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>s,contentTitle:()=>l,default:()=>b,frontMatter:()=>o,metadata:()=>i,toc:()=>c});var r=n(7462),a=(n(7294),n(3905));const o={sidebar_position:3},l="Kubernetes",i={unversionedId:"technologies/kubernetes",id:"technologies/kubernetes",title:"Kubernetes",description:"aliases",source:"@site/docs/technologies/kubernetes.md",sourceDirName:"technologies",slug:"/technologies/kubernetes",permalink:"/cocmd/docs/technologies/kubernetes",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/technologies/kubernetes.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Awscli",permalink:"/cocmd/docs/technologies/awscli"},next:{title:"Git",permalink:"/cocmd/docs/technologies/git"}},s={},c=[{value:"aliases",id:"aliases",level:2},{value:"paths",id:"paths",level:2},{value:"automations",id:"automations",level:3}],u={toc:c},p="wrapper";function b(e){let{components:t,...n}=e;return(0,a.kt)(p,(0,r.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"kubernetes"},"Kubernetes"),(0,a.kt)("h2",{id:"aliases"},"aliases"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-bash"},"alias k='kubectl'\nalias kgp='kubectl get pods'\nalias kgs='kubectl get svc'\nalias kgn='kubectl get nodes'\nalias kgc='kubectl get componentstatuses'\nalias kd='kubectl describe'\nalias krm='kubectl delete'\nalias kex='kubectl exec -it'\nalias klo='kubectl logs'\nalias kaf='kubectl apply -f'\nalias kdf='kubectl delete -f'\nalias kctx='kubectx'\nalias kns='kubens'\n\n")),(0,a.kt)("h2",{id:"paths"},"paths"),(0,a.kt)("h3",{id:"automations"},"automations"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"kubernetes.backup-configmaps")," - Backup all ConfigMaps in a namespace"),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"kubernetes.rolling-restart")," - Perform a rolling restart of a Deployment"),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("inlineCode",{parentName:"li"},"kubernetes.batch-pod-deletion")," - Batch delete Pods based on a label")))}b.isMDXComponent=!0}}]);
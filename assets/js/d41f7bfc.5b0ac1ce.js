"use strict";(self.webpackChunkwebsite=self.webpackChunkwebsite||[]).push([[8545],{3905:(e,r,t)=>{t.d(r,{Zo:()=>d,kt:()=>k});var o=t(7294);function n(e,r,t){return r in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t,e}function a(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);r&&(o=o.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,o)}return t}function c(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?a(Object(t),!0).forEach((function(r){n(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}function i(e,r){if(null==e)return{};var t,o,n=function(e,r){if(null==e)return{};var t,o,n={},a=Object.keys(e);for(o=0;o<a.length;o++)t=a[o],r.indexOf(t)>=0||(n[t]=e[t]);return n}(e,r);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(o=0;o<a.length;o++)t=a[o],r.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(n[t]=e[t])}return n}var s=o.createContext({}),l=function(e){var r=o.useContext(s),t=r;return e&&(t="function"==typeof e?e(r):c(c({},r),e)),t},d=function(e){var r=l(e.components);return o.createElement(s.Provider,{value:r},e.children)},u="mdxType",p={inlineCode:"code",wrapper:function(e){var r=e.children;return o.createElement(o.Fragment,{},r)}},m=o.forwardRef((function(e,r){var t=e.components,n=e.mdxType,a=e.originalType,s=e.parentName,d=i(e,["components","mdxType","originalType","parentName"]),u=l(t),m=n,k=u["".concat(s,".").concat(m)]||u[m]||p[m]||a;return t?o.createElement(k,c(c({ref:r},d),{},{components:t})):o.createElement(k,c({ref:r},d))}));function k(e,r){var t=arguments,n=r&&r.mdxType;if("string"==typeof e||n){var a=t.length,c=new Array(a);c[0]=m;var i={};for(var s in r)hasOwnProperty.call(r,s)&&(i[s]=r[s]);i.originalType=e,i[u]="string"==typeof e?e:n,c[1]=i;for(var l=2;l<a;l++)c[l]=t[l];return o.createElement.apply(null,c)}return o.createElement.apply(null,t)}m.displayName="MDXCreateElement"},2040:(e,r,t)=>{t.r(r),t.d(r,{assets:()=>s,contentTitle:()=>c,default:()=>p,frontMatter:()=>a,metadata:()=>i,toc:()=>l});var o=t(7462),n=(t(7294),t(3905));const a={sidebar_position:1},c="Docker",i={unversionedId:"technologies/docker",id:"technologies/docker",title:"Docker",description:"aliases",source:"@site/docs/technologies/docker.md",sourceDirName:"technologies",slug:"/technologies/docker",permalink:"/cocmd/docs/technologies/docker",draft:!1,editUrl:"https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/docs/technologies/docker.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Technologies",permalink:"/cocmd/docs/category/technologies"},next:{title:"Aws-s3",permalink:"/cocmd/docs/technologies/aws-s3"}},s={},l=[{value:"aliases",id:"aliases",level:2},{value:"paths",id:"paths",level:2},{value:"automations",id:"automations",level:3}],d={toc:l},u="wrapper";function p(e){let{components:r,...t}=e;return(0,n.kt)(u,(0,o.Z)({},d,t,{components:r,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"docker"},"Docker"),(0,n.kt)("h2",{id:"aliases"},"aliases"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-bash"},"alias d='docker'\nalias da='docker attach'\nalias dr='docker restart'\nalias dimg='docker images'\nalias dps='docker ps'\nalias dvol='docker volume ls'\nalias dclearimg='docker rmi $(docker images --quiet --filter \"dangling=true\")'\nalias dclearps='docker ps --filter status=dead --filter status=exited -aq | xargs docker rm -v'\nalias dclearvol='docker volume rm $(docker volume ls -qf dangling=true)'\nalias dc='docker-compose'\nalias dcer='docker-compose exec rails'\nalias dcerjasmine='docker-compose run --rm -e RAILS_ENV=test -p 8888:3000 rails rails jasmine'\nalias dcerspec='docker-compose run --rm -e RAILS_ENV=test rails rspec'\n\n")),(0,n.kt)("h2",{id:"paths"},"paths"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},"/users/morot/workspace/cocmd/cocmd_cli/resources/demo/docker/scripts"),(0,n.kt)("li",{parentName:"ul"},"/users/morot/workspace/cocmd/cocmd_cli/resources/demo/docker/bin")),(0,n.kt)("h3",{id:"automations"},"automations"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"docker.setup")," - setup docker for desktop"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"docker.cleanup")," - Cleanup Docker environment"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"docker.monitor")," - Monitor Docker resources"),(0,n.kt)("li",{parentName:"ul"},(0,n.kt)("inlineCode",{parentName:"li"},"docker.build-run")," - Build and run a Docker image")))}p.isMDXComponent=!0}}]);
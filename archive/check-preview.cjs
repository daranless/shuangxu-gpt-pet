const fs=require('fs'),path=require('path'),vm=require('vm');
const root=path.resolve(__dirname,'..'),html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const elements={};
function elem(){return {style:{},textContent:'',value:0,children:[],classList:{toggle(){}},append(x){this.children.push(x)}};}
['#pet','#info','#play','#direction','#states','#look','#scale'].forEach(k=>elements[k]=elem());
const context={document:{querySelector:k=>elements[k],querySelectorAll:()=>elements['#states'].children,createElement:elem},setTimeout:()=>1,clearTimeout:()=>{}};
vm.createContext(context);vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],context);
const assert=(x,m)=>{if(!x)throw Error(m)};
assert(elements['#states'].children.length===9,'nine states');assert(elements['#direction'].children.length===16,'sixteen directions');
for(let i=0;i<9;i++){elements['#states'].children[i].onclick();assert(elements['#pet'].style.backgroundPosition===`0px ${-i*208}px`,'row position '+i);}
for(let i=0;i<16;i++){elements['#direction'].value=i;elements['#direction'].onchange();assert(elements['#pet'].style.backgroundPosition===`${-(i%8)*192}px ${-(9+Math.floor(i/8))*208}px`,'direction '+i);}
elements['#look'].onclick();assert(elements['#play'].textContent==='暂停','look playback');elements['#play'].onclick();assert(elements['#play'].textContent==='播放','pause');
const resources=[...html.matchAll(/(?:src|href)="([^"]+)"/g)].map(m=>m[1]);resources.push('outputs/shuangxu-spritesheet.png');for(const r of resources)assert(fs.existsSync(path.join(root,r)),'resource '+r);
console.log(JSON.stringify({ok:true,stateButtons:9,directions:16,localResources:resources.length,checks:['script syntax','state selection','direction selection','play/pause','local resource paths']},null,2));

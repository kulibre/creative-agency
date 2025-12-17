var x=Object.defineProperty;var m=(n,e,t)=>e in n?x(n,e,{enumerable:!0,configurable:!0,writable:!0,value:t}):n[e]=t;var i=(n,e,t)=>m(n,typeof e!="symbol"?e+"":e,t);var E="__framer_force_showing_editorbar_since",T="__framer_editor_button_position",a="2147483647";var b=300;var s=12,l="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAApNJREFUSA2tlUtLlFEYgEe7mtFFQ8NLFBG1SJAwahtiLVy5ceVSEPQH1LZf0Lp9FO1bdYNyI7gyBFcS2kAzilYq3sfxeYZ55Zv6FGfohWfOd97vnPd23u9MXeZoaeb1Q7gPHXAFzsAS5GACxiEPqVKXqs1kmtAPQi+cAtedToz1PJ8ExxPwDl7CAlRImoN7rBiF86ABHTiGAzMIh8n3O+ifwWc4EL0n5TGTYQijvjNSxbUadozInUeGZ3nuh1WYgpIkM+hGMwYajAgdrfUn+AaLoLTCAxiAOxCZxL4RdB+gZMjxEjwHo4hS8Jh5DR9hz0mKaNizegoNEI7Wee6FXJTISG6AUgDr+QImoAiHie+mwZJow/PRps4uwnsnRj8Epqc4voVJJ8eULOtW4BFYYjPpgjc+3IWI2sh/wFeoVl6xYQ48dDGLfjOwc/ygQqz595hUMVouS9QHBm4l6k3HWpnBLqicgVrlCxujSbR1Swd+UDpQYRS/oVaZZ2MWwlZBB9Zdxf+QTYw8SRgq6sAvz7vH6JULEB9USVHFjzZskgPRQR4ayxoXXIdaHdg9HrB2rErByWxZERnYtrWUzD0esDbtTmXPhzXwHrKLxEUbYGbVyDkWWwkdadfqbPmwDXZSCyh2VAf8BM/nOOJH5Y0QopMt2I5U/KO4DZZJB47XwEX+ex0mGroMV8sLwp56gyuGwiyW4SZ4c8bt2cZzO7jBNeqtsRHbeZ1g9krsMbhfYPv/c5gecA+4yAVuitFszE5Hjva872OMdXagF19JIoOYWyozMTI3J0tmA6gLvXPfO1cc/XOqOLe/HbjwD8yCXRD3VNJROEgatiRZMJsKsbZHia3nAdphtq8fkiWyXJbBe8uM1aXKPouNnz2Bm1kwAAAAAElFTkSuQmCC",g="__framer-editorbar-container",c="__framer-editorbar-label",f="__framer-editorbar-button",h="__framer-editorbar-loading-spinner",w="__framer-editorbar-button-tooltip-visible",O=`
#${g} {
    align-items: center;
    display: flex;
    gap: 8px;
    position: fixed;
    z-index: calc(${a});
    width: max-content;
    cursor: pointer;
}

#${c} {
    background-color: #111;
    border-radius: 8px;
    font-family: "Inter", "Inter-Regular", system-ui, Arial, sans-serif;
    font-size: 12px;
    height: fit-content;
    opacity: 0;
    padding: 4px 8px;
    transition: opacity 0.4s ease-out;
    font-weight: 500;
    flex-shrink: 0;
    position: fixed;
    width: max-content;
    pointer-events: none;
    user-select: none;
}

#${f} {
    all: unset;
    align-items: center;
    border-radius: 15px;
    display: flex;
    height: 30px;
    justify-content: center;
    width: 30px;
    flex-shrink: 0;
}

#${c}.${w} {
    opacity: 1;
}

#${c}, #${f} {
    backdrop-filter: blur(10px);
    background-color: rgba(34, 34, 34, 0.8);
    box-shadow: rgba(0, 0, 0, 0.1) 0px 2px 4px 0px, rgba(0, 0, 0, 0.05) 0px 1px 0px 0px, rgba(255, 255, 255, 0.15) 0px 0px 0px 1px;
    color: #fff;
}

#${h} {
    width: ${s}px;
    height: ${s}px;
    -webkit-mask: url(${l});
    mask: url(${l});
    -webkit-mask-size: ${s}px;
    mask-size: ${s}px;
    background-color: #fff;


    animation-duration: 800ms;
    animation-iteration-count: infinite;
    animation-name: __framer-loading-spin;
    animation-timing-function: linear;
}

@keyframes __framer-loading-spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
`,_=document.createElement("style");_.innerHTML=O;document.head.appendChild(_);var p=class extends Promise{constructor(){let t,r;super((o,u)=>{t=o,r=u});i(this,"_state","initial");i(this,"resolve");i(this,"reject");this.resolve=o=>{this._state="fulfilled",t(o)},this.reject=o=>{this._state="rejected",r(o)}}get state(){return this._state}pending(){return this._state="pending",this}isResolved(){return this._state==="fulfilled"||this._state==="rejected"}};p.prototype.constructor=Promise;function A(n){let e=window.__framer_editorBarDependencies;if(!e)throw new Error("Dependencies not found");if(e.__version<1||e.__version>3)throw new Error("Unsupported version");let t=e[n];if(!t)throw new Error("Dependency not found");return t}var{createElement:d,memo:j,useCallback:P,useEffect:Z,useRef:X,useState:U,useLayoutEffect:Y}=A("react");function C(n,e,t){let{children:r,...o}=e??{};return t!==void 0&&(o.key=t),d(n,o,r)}function F(n,e,t){let{children:r,...o}=e??{};return t!==void 0&&(o.key=t),d(n,o,...r)}function G(n,...e){if(n)return;let t=Error("Assertion Error"+(e.length>0?": "+e.join(" "):""));if(t.stack)try{let r=t.stack.split(`
`);r[1]?.includes("assert")?(r.splice(1,1),t.stack=r.join(`
`)):r[0]?.includes("assert")&&(r.splice(0,1),t.stack=r.join(`
`))}catch{}throw t}function W(n,e){throw e||new Error(n?`Unexpected value: ${n}`:"Application entered invalid state")}export{i as a,E as b,T as c,a as d,b as e,g as f,c as g,f as h,h as i,w as j,p as k,A as l,j as m,P as n,Z as o,X as p,U as q,G as r,W as s,C as t,F as u};
//# sourceMappingURL=../app.framerstatic.com/chunk-KNMSEEX6.mjs.map

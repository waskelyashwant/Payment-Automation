(this.webpackJsonpbill_pay=this.webpackJsonpbill_pay||[]).push([[0],{30:function(e,t,c){},31:function(e,t,c){},55:function(e,t,c){"use strict";c.r(t);var n=c(0),i=c.n(n),l=c(5),a=c.n(l),s=(c(30),c(8)),r=(c(31),c(19)),o=c.n(r),j=c(69),d=c.p+"static/media/bill_file.7633a66d.jpg",h=c.p+"static/media/card_file.84e983d2.jpg",u=c(1);var b=function(){var e=Object(n.useState)(),t=Object(s.a)(e,2),c=t[0],i=t[1],l=Object(n.useState)(),a=Object(s.a)(l,2),r=a[0],b=a[1],f=Object(n.useState)(!1),p=Object(s.a)(f,2),x=p[0],O=p[1],m=Object(n.useState)(!1),v=Object(s.a)(m,2),S=v[0],y=v[1];return Object(u.jsxs)("div",{className:"App",children:[Object(u.jsxs)("div",{className:"run",children:[Object(u.jsx)(j.a,{variant:"outlined",color:"primary",onClick:function(){fetch("/status2").then((function(e){return e.json()})).then((function(e){0===e.value?alert(e.code):fetch("/billCheck").then((function(e){return e.json()})).then((function(e){alert(e.code)}))}))},children:"Bill Check"}),Object(u.jsx)("span",{children:" "}),Object(u.jsx)(j.a,{variant:"outlined",color:"secondary",onClick:function(){fetch("/stopScript2").then((function(e){return e.json()})).then((function(e){alert(e.code)}))},children:"Stop Bill Check"})]}),Object(u.jsxs)("div",{children:[Object(u.jsx)("h3",{children:"Bill excel file should have same column name as given below."}),Object(u.jsx)("img",{src:d,alt:"bill file format"})]}),Object(u.jsxs)("div",{className:"d-flex",children:[Object(u.jsxs)("h4",{children:["Select Bill Details ( Excel File (",Object(u.jsx)("span",{style:{color:"red"},children:" .xlsx"})," format) )"]}),Object(u.jsx)("input",{className:"input",type:"file",name:"file",placeholder:"Bill Details (Excel File))",onChange:function(e){i(e.target.files[0]),O(!0)}}),x?Object(u.jsx)("div",{children:Object(u.jsxs)("p",{children:["Filename: ",c.name]})}):Object(u.jsx)("p",{children:"Select a file to show details"})]}),Object(u.jsx)("br",{}),Object(u.jsxs)("div",{children:[Object(u.jsx)("h3",{children:"Card details excel file should have same column name as given below."}),Object(u.jsx)("img",{src:h,alt:"Card details file format"}),Object(u.jsxs)("div",{className:"d-flex",children:[Object(u.jsxs)("h4",{children:[" ","Select Card Details ( Excel File (",Object(u.jsx)("span",{style:{color:"red"},children:" .xlsx"})," format) )"]}),Object(u.jsx)("input",{className:"input",type:"file",name:"file",placeholder:"Bill Details (Excel File))",onChange:function(e){b(e.target.files[0]),y(!0)}}),S?Object(u.jsx)("div",{children:Object(u.jsxs)("p",{children:["Filename: ",r.name]})}):Object(u.jsx)("p",{children:"Select a file to show details"})]})]}),Object(u.jsx)("div",{children:c&&r&&Object(u.jsx)(j.a,{variant:"outlined",color:"primary",onClick:function(){var e=new FormData;e.append("file",c),e.append("file2",r),o.a.post("/sendFile",e).then((function(e){alert(e.data.code)}))},children:"Upload Files"})}),Object(u.jsx)("div",{className:"run",children:Object(u.jsx)(j.a,{variant:"outlined",color:"primary",onClick:function(){fetch("/status").then((function(e){return e.json()})).then((function(e){0===e.value?alert(e.code):fetch("/runScript").then((function(e){return e.json()})).then((function(e){alert(e.code)}))}))},children:"Run Script"})}),Object(u.jsx)("div",{style:{marginTop:"10px"},children:Object(u.jsx)(j.a,{variant:"outlined",color:"secondary",onClick:function(){fetch("/stopScript").then((function(e){return e.json()})).then((function(e){alert(e.code)}))},children:"Stop Script"})})]})};a.a.render(Object(u.jsx)(i.a.StrictMode,{children:Object(u.jsx)(b,{})}),document.getElementById("root"))}},[[55,1,2]]]);
//# sourceMappingURL=main.5b45b526.chunk.js.map
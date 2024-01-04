(: declare option saxon:output "indent=yes"; :)
<result>
({
for $l in //.
where local-name($l) eq 'label'
return 
concat(concat('"',data($l)),'",')
})
</result>
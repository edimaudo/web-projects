### Brief

Professor Oak is in trouble! A wild Blastoise wreaked havoc in the server room and destroyed every single machine. There are no backups - everything is lost! Professor Oak quickly scribbles down all the Pokémon from memory and hands them to you on a piece of paper.  Your task is to restore the Pokémon Database from that file and create a Pokémon API so that they’re never lost again.

### Tasks
- Create one API endpoint `/pokemon`
- This API endpoint should be searchable, filterable and paginatable
    -   Search: name
    -   Filter: HP, Attack & Defense
        -   e.g. `/pokemon?hp[gte]=100&defense[lte]=200`
    -   Pagination: e.g. `/pokemon?page=1`





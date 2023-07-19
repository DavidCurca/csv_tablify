# csv_tablify

converts a csv file that represents some sort of ranking into a pdf similar to ones by [sepi](https://sepi.ro). when used the `static` folder, csv data and images should be in the same folder as the script.

**Note**, if the tasks are not from [kilonova](https://kilonova.ro), in the config file the variables for links to the tasks are `task_1`, `task_2`, ... and not `task_ids`.

## prerequisites

[wkhtmltopdf](https://wkhtmltopdf.org/), babel

## customization

the template used to generate the pdfs is in the `static` folder.
#!/bin/sh
#Added by Vimos 2013-09-12
#report_type 可以为 user.umeng,download
report_type=$1
report_date=$2
. ~/.profile
report=$MassQueryPath/demos/report/${report_type}_report.html
log=$MassQueryPath/log/tmp/${report_type}.log

#Delete old report
rm $report
#Generate new report
python $MassQueryPath/demos/gen_${report_type}_report.py ${report_date}
#If no report is produced, send error log to Vimos
if [ -f $report ]; then
    cat $report | python $MassQueryPath/demos/send_report.py ${report_type} ${report_date}
else
    cat log | mail -s "no $report" zhaoxuhui@appchina.com 
fi

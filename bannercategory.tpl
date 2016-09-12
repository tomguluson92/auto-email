<b> banner分类点击下载的数据 </b>
<table cellspacing="0" width="100%" border="1">
    <tr bgcolor="silver">
        <td align=center rowspan=1>日期</td>
        <td align=center rowspan=1>游戏类型</td>
        <td align=center colspan=1>点击人数</td>
        <td align=center colspan=1>点击次数</td>
        <td align=center colspan=1>下载人数</td>
        <td align=center colspan=1>下载次数</td>
        <td align=center colspan=1>点击人数转化率</td>
        <td align=center colspan=1>点击次数转化率</td>
        <td align=center colspan=1>人均下载次数</td>
    </tr>
    % for val in data_list:
        <tr>
            <td align=center >${val.get('date')}</td>
            <td align=center >${val.get('baidu_counts')}</td>
            <td align=center >${val.get('appchina_counts')}</td>
            <td align=center >${val.get('anticheat_baidu_counts')}</td>
            <td align=center >${val.get('anticheat_appchina_counts')}</td>
            <td align=center >${val.get('rate')}%</td>
            <td align=center >${val.get('rate')}%</td>
            <td align=center >${val.get('rate')}%</td>
        </tr>
    % endfor
</table>
</br>
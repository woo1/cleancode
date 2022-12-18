## magig method
<table>
<thead>
    <tr>
        <th>예시</th>
        <th>매직메서드</th>
        <th>파이썬 개념</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>obj[key], obj[i:j], obj[i:j:k]</td>
        <td>__getitem__(key)</td>
        <td>첨자형(subscriptable) 객체</td>
    </tr>
    <tr>
        <td>with obj: ...</td>
        <td>__enter__ / __exit__</td>
        <td>컨텍스트 관리자</td>
    </tr>
    <tr>
        <td>for i in obj: ...</td>
        <td>__iter__ / __next__, __len__ / __getitem__</td>
        <td>이터러블 객체, 시퀀스</td>
    </tr>
    <tr>
        <td>obj.attribute</td>
        <td>__getattr__</td>
        <td>동적 속성 조회</td>
    </tr>
    <tr>
        <td>obj(*args, **kargs)</td>
        <td>__call__(*args, **kargs)</td>
        <td>호출형(callable) 객체</td>
    </tr>
</tbody>
</table>
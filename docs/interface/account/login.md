##用户登陆接口

###请求地址
/account/user/login
####请求方式
POST
###请求参数
<table>
    <thead>
        <tr>
            <th>字段</th>
            <th>说明</th>
            <th>是否为空</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>username</td>
            <td>用户名</td>
            <td>否</td>
        </tr>
        <tr>
            <td>password</td>
            <td>密码</td>
            <td>否</td>
        </tr>
    </tbody>
</table>

### 返回结果
```
{
    "data": {
        "id": 1,
        "rid": 0,
        "username": "zxczxc",
        "stuNum": "201719044228",
        "token": ""
    },
    "meta": {
        "msg": "登陆成功",
        "statu": "200"
    }
}
```
###返回字段说明
<table>
    <thead>
        <tr>
            <th>字段</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>data</td>
            <td>dict</td>
            <td>用户信息</td>
        </tr>
        <tr>
            <td>id</td>
            <td>int</td>
            <td>用户ID</td>
        </tr>
        <tr>
            <td>rid</td>
            <td>int</td>
            <td>用户角色ID</td>
        </tr>
        <tr>
            <td>username</td>
            <td>String</td>
            <td>用户名</td>
        </tr>
        <tr>
            <td>token</td>
            <td></td>
            <td></td>
        </tr> 
    </tbody>
</table>

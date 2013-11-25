<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link href="../static/style.css" media="screen" rel="stylesheet" type="text/css" />
<title>{{dictionary['name']}}</title>
   </head>
    <body>
    <h1>{{dictionary['name']}} !</h1>
<table>
      <tbody>
        <tr>
          <td>local name</td>
          <td>{{dictionary['local-name']}}</td>
</tr>
        <tr>
          <td>top level domain</td>
          <td>
% domain=dictionary['top-level-domain'].split(',')
% for d in domain:
    <span class="domain">{{d[1:]}}</span>
% end
</td>
</tr>
 <tr>
          <td>calling code</td>
          <td>{{dictionary['calling-code']}}</td>
</tr>
 <tr>
          <td>capital city</td>
          <td>{{dictionary['capital-city']}}</td>
</tr>
 <tr>
          <td>region</td>
          <td>{{dictionary['region']}}</td>
</tr>
 <tr>
          <td>subregion</td>
          <td>{{dictionary['subregion']}}</td>
</tr>
 <tr>
          <td>language</td>
          <td>{{dictionary['language']}}</td>
</tr>
</tbody>
    </table>
    </body>
</html>


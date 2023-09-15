{% extends "mail_templated/base.tpl" %}

{% block subject %}
{{subject}}}
{% endblock %}

{% block body %}
Dashboard and Do: New Message <br/><br/>
--------------------------------------------------
Dear Site Administrator: <br/><br/>

{{ body_message }} <br/><br/>

From <br/>
&nbsp;&nbsp; {{ senders_name }}, <br/><br/>
--------------------------------------------------
:: Message Details ::
This message was sent by sender: {{from_email}}. <br/>
This message was sent by: {{ site_name }}. <br/>
This message was sent from: {{ site_url }}. <br/>
The message was sent at: {{ datetime }}. <br/><br/>
--------------------------------------------------
To view this message as HTML, toggle HTML views in your mail client.
{% endblock %}

{% block html %}
<h3> Dashboard and Do: New Message</h3>
<hr>
<div>
    <p>Dear Site Administrator: </p>
    <p>{{ html_message }}</p>
    <p>Hello {{ name }}</p>
</div>
<hr>
<div>
    <p><small>This message was sent by sender: <strong>{{from_email}}</strong>.</small> </p>
    <p><small>This message was sent by <em>{{ site_name }}</em>.</small></p>
    <p><small>This message was sent from <em>{{ site_url }}</em>.</small></p>
    <p><small>The message was sent at <strong>{{ datetime }}</strong>.</small></p>
</div>
<p> To view this message as plain text, toggle HTML views in your mail client.</p>
{% endblock %}

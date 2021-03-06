#!/bin/sh


. /usr/lib/libmodcgi.sh

check "$STUNNEL_ENABLED" yes:auto_c "*":man_c

for i in crit err warning notice info debug; do
	select "$STUNNEL_VERBOSE" "$i":verbose_${i}
done

sec_begin '$(lang de:"Starttyp" en:"Start type")'

cat << EOF
<p>
<input id="e1" type="radio" name="enabled" value="yes"$auto_c_chk><label for="e1"> $(lang de:"Automatisch" en:"Automatic")</label>
<input id="e2" type="radio" name="enabled" value="no"$man_c_chk><label for="e2"> $(lang de:"Manuell" en:"Manual")</label>
</p>
EOF

sec_end
sec_begin '$(lang de:"Konfiguration" en:"Configuration")'

cat << EOF
<h2>$(lang de:"Erweiterte Einstellungen" en:"Advanced settings"):</h2>
<p>$(lang de:"OpenSSL Optionen" en:"OpenSSL options"): <input id="ssloptions" type="text" name="ssloptions" size="20" maxlength="255" value="$(html "$STUNNEL_SSLOPTIONS")"></p>
<p>$(lang de:"Log-Level" en:"Verbosity level"):
<select name='verbose'>
<option value="crit"$verbose_crit_sel>0</option>
<option value="err"$verbose_err_sel>1</option>
<option value="warning"$verbose_warning_sel>2</option>
<option value="notice"$verbose_notice_sel>3</option>
<option value="info"$verbose_info_sel>4</option>
<option value="debug"$verbose_debug_sel>5</option>
</select>
</p>
EOF
sec_end
sec_begin '$(lang de:"Dienste" en:"Services")'

cat << EOF
<ul>
<li><a href="$(href file stunnel svcs)">$(lang de:"Dienste bearbeiten" en:"Edit services file")</a></li>
<li><a href="$(href file stunnel certchain)">$(lang de:"Zertifikats-Kette bearbeiten" en:"Edit certificate chain")</a></li>
<li><a href="$(href file stunnel key)">$(lang de:"Privaten Schl�ssel bearbeiten" en:"Edit private key")</a></li>
</ul>
EOF
sec_end

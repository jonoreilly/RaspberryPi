<?php

	session_start();

	if ( empty($_SESSION["init"]) || $_GET["value"] == "init")
	{
		$_SESSION["init"] = "init";
		system ( "gpio mode 1 pwm" );
		system ( "gpio pwm-ms" );
		system ( "gpio pwmc 400" );
		system ( "gpio pwmr 1000" );
		system ( "gpio mode 29 out" );
		system ( "gpio write 29 0" );
	}

	if (!empty( $_GET["value"] ))
	{
		system ( "gpio pwm 1 ".$_GET["value"] );
	}

	if (!empty( $_GET["laser"] ))
	{
		if ($_GET["laser"] == "on") { system ( "gpio write 29 1" ); }
		else 			    { system ( "gpio write 29 0" ); }
	}




?>


<br>
<br>
<br>

<a href="?value=init"> Init </a>

<table>

	<tr>

		<td>
			<a href="?value=1"> 0 </a>
		</td>


		<td>
			<a href="?laser=on"> Laser On </a>
		</td>
	</tr>

	<tr>
		<td>
			<a href="?value=25"> 25 </a>
		</td>

		<td>
			<a href="?laser=off"> Laser Off </a>
		</td>
	</tr>

	<tr>
		<td>
			<a href="?value=50"> 50 </a>
		</td>
	</tr>

	<tr>
		<td>
			<a href="?value=75"> 75 </a>
		</td>
	</tr>

	<tr>
		<td>
			<a href="?value=100"> 100 </a>
		</td>

	</tr>

        <tr>
                <td>
                        <a href="?value=125"> 125 </a>
                </td>

        </tr>


</table>





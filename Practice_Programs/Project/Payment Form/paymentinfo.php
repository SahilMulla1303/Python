<?php
$servername = "127.0.0.1";
$username = "root";
$password = "";
$dbname = "collegeproject";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$FullName=$_POST["FName"];
$Gender=$_POST["Gender"];
$DOB=$_POST["DOB"];
$MobNo=$_POST["MobNo"];
$Email=$_POST["Email"];
$Address=$_POST["Address"];
$CardNo=$_POST["CardNo"];
$CardType=$_POST["CardType"];
$CvvNo=$_POST["CvvNo"];
$ExpireDate=$_POST["ExpirDate"];

$sql = "INSERT INTO paymentform(FullName,Gender,DOB,MobileNo,Email,Address,CardNo,CardType,CvvNo,ExpireDate)
value('".$FullName."','".$Gender."','".$DOB."',".$MobNo.",'".$Email."','".$Address."',".$CardNo.",'".$CardType."','".$CvvNo."','".$ExpireDate."')";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
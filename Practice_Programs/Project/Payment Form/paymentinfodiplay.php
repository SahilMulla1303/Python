<!DOCTYPE html>
<html>
<head>
    <title>Display Data</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
    <table border="1px solid">
        <tr>
            <th>Id</th>
            <th>Full Name</th>
            <th>Gender</th>
            <th>DOB</th>
            <th>MobNo</th>
            <th>Email</th>
            <th>Address</th>
            <th>CardNo</th>
            <th>CardType</th>
            <th>CvvNo</th>
            <th>ExpirationDate</th>
        </tr>
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
              

        $sql = "SELECT * FROM paymentform";
        $result=$conn->query($sql);

        if (!$result) {
          die("Invalid query:".$connection->error);
        } 

        while($row=$result->fetch_assoc()){

            echo "<tr>
            <td>".$row["id"]."</td>
            <td>".$row["FullName"]."</td>
            <td>".$row["Gender"]."</td>
            <td>".$row["DOB"]."</td>
            <td>".$row["MobileNo"]."</td>
            <td>".$row["Email"]."</td>
            <td>".$row["Address"]."</td>
            <td>".$row["CardNo"]."</td>
            <td>".$row["CardType"]."</td>
            <td>".$row["CvvNo"]."</td>
            <td>".$row["ExpireDate"]."</td>
            </tr>";
        }
        ?>
    </table>

</body>
</html>
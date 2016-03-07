<script>
        $(function() {
            $("#mainUl").children("li").click(function() {
                var clone = $(this).clone();
                clone.append("<span style='color:red;font-weight: bold;cursor:pointer'> X</span>")
                    .find("span").click(function () {
                    $(this).parent().remove("li");
                });
                $("#showUl").append(clone);
            });
        });
    </script>
    <body>
        <div style="float: left">
            <ul id="mainUl">
                <li>标题1</li>
                <li >标题2</li>
                <li >标题3</li>
                <li >标题4</li>
                <li >标题5</li>
            </ul>
        </div>
        <div style="float: left">
            <ul id="showUl">
            </ul>
        </div>
    </body>

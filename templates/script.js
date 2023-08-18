$(document).ready(function () {
    $("#hybridize-form").submit(function (event) {
        event.preventDefault();

        var parent1Height = $("#parent1_height").val();
        var parent1Color = $("#parent1_color").val();
        // Collect more parent traits

        var parent2Height = $("#parent2_height").val();
        var parent2Color = $("#parent2_color").val();
        // Collect more parent traits

        $.post("/hybridize", {
            parent1_height: parent1Height,
            parent1_color: parent1Color,
            // Pass more parent traits

            parent2_height: parent2Height,
            parent2_color: parent2Color,
            // Pass more parent traits
        }, function (data) {
            $("#parent1-traits").empty().append(data.parent1_traits);
            $("#parent2-traits").empty().append(data.parent2_traits);
            $("#child-traits").empty().append(data.child_traits);
            $("#result").show();
        });
    });
});

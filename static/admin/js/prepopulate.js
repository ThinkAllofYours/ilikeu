<<<<<<< HEAD
/*global URLify*/
(function($) {
    'use strict';
    $.fn.prepopulate = function(dependencies, maxLength, allowUnicode) {
=======
(function($) {
    $.fn.prepopulate = function(dependencies, maxLength) {
>>>>>>> 79cfd5b0f53f841b9da29c33522c5da05c9d58d6
        /*
            Depends on urlify.js
            Populates a selected field with the values of the dependent fields,
            URLifies and shortens the string.
            dependencies - array of dependent fields ids
            maxLength - maximum length of the URLify'd string
<<<<<<< HEAD
            allowUnicode - Unicode support of the URLify'd string
=======
>>>>>>> 79cfd5b0f53f841b9da29c33522c5da05c9d58d6
        */
        return this.each(function() {
            var prepopulatedField = $(this);

<<<<<<< HEAD
            var populate = function() {
=======
            var populate = function () {
>>>>>>> 79cfd5b0f53f841b9da29c33522c5da05c9d58d6
                // Bail if the field's value has been changed by the user
                if (prepopulatedField.data('_changed')) {
                    return;
                }

                var values = [];
                $.each(dependencies, function(i, field) {
                    field = $(field);
                    if (field.val().length > 0) {
                        values.push(field.val());
                    }
                });
<<<<<<< HEAD
                prepopulatedField.val(URLify(values.join(' '), maxLength, allowUnicode));
=======
                prepopulatedField.val(URLify(values.join(' '), maxLength));
>>>>>>> 79cfd5b0f53f841b9da29c33522c5da05c9d58d6
            };

            prepopulatedField.data('_changed', false);
            prepopulatedField.change(function() {
                prepopulatedField.data('_changed', true);
            });

            if (!prepopulatedField.val()) {
                $(dependencies.join(',')).keyup(populate).change(populate).focus(populate);
            }
        });
    };
})(django.jQuery);

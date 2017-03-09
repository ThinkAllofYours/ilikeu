<<<<<<< HEAD
/*global django:true, jQuery:false*/
=======
>>>>>>> 79cfd5b0f53f841b9da29c33522c5da05c9d58d6
/* Puts the included jQuery into our own namespace using noConflict and passing
 * it 'true'. This ensures that the included jQuery doesn't pollute the global
 * namespace (i.e. this preserves pre-existing values for both window.$ and
 * window.jQuery).
 */
var django = django || {};
django.jQuery = jQuery.noConflict(true);

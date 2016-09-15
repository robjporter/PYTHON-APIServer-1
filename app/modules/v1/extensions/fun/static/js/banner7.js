(function () {
    $('.box').velocity('transition.slideDownIn', {
        stagger: 250,
        drag: true,
        duration: 2000,
        complete: function () {
            return $('.value').each(function (index, item) {
                var val, value;
                value = $(item).data('value');
                val = parseInt(value, 10);
                return $({ someValue: 0 }).animate({ someValue: val }, {
                    duration: 1000,
                    easing: 'swing',
                    step: function () {
                        return $(item).text(Math.round(this.someValue));
                    }
                });
            });
        }
    });
}.call(this));

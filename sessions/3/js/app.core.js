
if (typeof muzik === undefined) {
    var muzik = {};
}

var intv = 0;
muzik = {
    play: function() {
        $('#play').on('playMusic', function() {
            $('#player')[0].play();
            //$('#song-time').html(convert_milliseconds_to_min_and_seconds($('#player')[0].currentTime));
            $('#sliderTime')[0].max = $('#player')[0].duration;
            intv = setInterval(this.updateSlider, 100);
            console.log('Music is playing');

        });

        $('#play').on('click', function() {
            $('#play').trigger('playMusic');
        });
    },

    pause: function() {
        $('#pause').on('pauseMusic', function() {
            $('#player').trigger('pause');
            clearInterval(intv);
            console.log('Music is paused');
        });

        $('#pause').on('click', function() {
            $('#pause').trigger('pauseMusic');
        });
    },

    stopPlaying: function() {
        $('#stop').on('stopMusic', function() {
            $('#player').trigger('pause');
            $('#player')[0].currentTime = 0;
            $('#sliderTime')[0].value = 0;
            clearInterval(intv);
            console.log('Music is stopped');
        });

        $('#stop').on('click', function() {
            $('#stop').trigger('stopMusic');
        });
    },

    volume: {
        volumeUp: function() {
            $('#vup').on('vup', function() {
                if ($('#player')[0].volume < 1) {
                    $('#player')[0].volume += 0.1;
                    console.log($('#player')[0].volume);
                } else {
                    $('#player')[0].volume = 1;
                    console.log($('#player')[0].volume);
                }
            });

            $('#vup').on('click', function() {
                console.log('increasing the volume');
                $('#vup').trigger('vup');
            });
        },
        volumeDown: function() {
            $('#vdown').on('vdown', function() {
                if ($('#player')[0].volume > 0) {
                    $('#player')[0].volume -= 0.1;
                    console.log($('#player')[0].volume);
                } else {
                    $('#player')[0].volume = 0;
                    console.log($('#player')[0].volume);
                }
            });

            $('#vdown').on('click', function() {
                console.log('decreasing the volume');
                $('#vdown').trigger('vdown');
            });
        }
    },
    updateSlider: function() {
        //console.log('Updating slider value');
        $('#sliderTime')[0].value = $('#player')[0].currentTime;
        $('#song-time').html(convert_milliseconds_to_min_and_seconds($('#player')[0].currentTime));
        //console.log('slide-time value : ' + $('#sliderTime')[0].value);
    },
    repeatCall: function() {
        intv = setInterval(this.updateSlider, 100);
    }
};

var convert_milliseconds_to_min_and_seconds = function(ms) {
    var seconds = (((ms % 31536000) % 86400) % 3600) % 60;
    var minutes = Math.floor((((ms % 31536000) % 86400) % 3600) / 60);
    var sTime = (seconds >= 10) ? (minutes + ":" + Math.round(seconds)) : (minutes + ":0" + Math.round(seconds));

    return "Time Elapsed: " + sTime;
};

// when the document (DOM) is ready
$(function() {
    muzik.play();
    muzik.pause();
    muzik.stopPlaying();
    muzik.volume.volumeDown();
    muzik.volume.volumeUp();

    //
    // Reposition the music when clicked on the slider
    //////////////////////////////////////////////////
    $('#sliderTime').on('change', function() {
        console.log('Setting the current time with : ' + $('#sliderTime')[0].value);
        $('#player')[0].currentTime = $('#sliderTime')[0].value;
    });

    muzik.repeatCall();
});

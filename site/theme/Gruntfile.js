module.exports = function(grunt) {
    grunt.initConfig({

        // Options:
        // https://github.com/gruntjs/grunt-contrib-less
        less: {
            development: {
                options: {
                    paths: ["less"],
                    sourceMap: true,
                    sourceMapFilename: "assets/css/theme.css.map",
                    sourceMapBasepath: "css",
                    sourceMapRootpath: "..",
                    sourceMapURL: "theme.css.map"
                },
                files: {
                    "assets/css/main.css": "assets/less/main.less"
                },
            },
            production: {
                options: {
                  paths: ["assets/css"],
                  cleancss: true,
                  // NO KNEELING TOWARDS REDMOND
                  ieCompat: false
                },
                files: {
                    "assets/css/main.min.css": "assets/less/main.less"
                }
            }
        },
        watch: {
            files: "./assets/less/*",
            tasks: ["less"]
        }
    });
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('production', ['less:production']);
};
module.exports = function(grunt) {
  var config = {};

  //src ===============================
  var src;
  config.src = src = {
    sassMain: 'themes/malt/scss/main.scss',
    distFolder: 'themes/malt/public/stylesheets/it-in-dublin.dist.css',
    devFolder: 'themes/malt/public/stylesheets/it-in-dublin.dev.css',
    sassFolder: 'themes/malt/scss/**/*.scss',
    serverPort: 8000
  };

  //Watch ===============================
  config.watch = {
    scripts: {
      files: ["<%= src.sassFolder %>"],
      tasks: ["sass:dist"]
    }
  }

  //Sass ===============================
  var sass;
  config.sass = sass = {};

  //sass distribution
  sass.dist = {
    options: {
      style: "compressed",
      noCache: true,
      sourcemap: 'none',
      update: true
    },
    files: {
      "<%= src.distFolder %>": "<%= src.sassMain %>"
    }
  };

  //sass development env.
  sass.dev = {
    options: {
      style: "expanded",
      lineNumber: true,
    },
    files: {
      "<%= src.devFolder %>": "<%= src.sassMain %>"
    }
  };


  var cssmin
    config.cssmin = {
        target: {
            files: [{
                expand: true,
                cwd: 'themes/malt/static/css',
                src: ['*.css', '!*.min.css'],
                dest: 'themes/malt/static/css/',
                ext: '.min.css'
            }]
        }
    }



  //grunt serve ===============================
  config.connect = {
    server: {
      options: {
        livereload: true,
        port: "<%= src.serverPort %>"
      }
    }
  };

  //Register custom tasks ===============================
  grunt.registerTask('default', ['dev']);
  grunt.registerTask('dev', ['sass:dev']);
  grunt.registerTask('dist', ['sass:dist']);
  grunt.registerTask('serve', ['connect:server', 'watch']);
  require('time-grunt')(grunt);
  require('load-grunt-tasks')(grunt, {
    scope: 'devDependencies'
  });

  //General setup ===============================
  grunt.initConfig(config);

};

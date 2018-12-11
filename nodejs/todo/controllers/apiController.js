var Todos = require('../models/todoModel');
var bodyParser = require('body-parser');

module.exports = function(app) {
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({extended: false}));
    app.get('/api/todos/:uname', function(req, res) {
        Todos.find({username:req.params.uname},
                   function(err, todos) {
                       if (err) throw err;

                       res.send(todos);
        });
    });

    app.get('/api/todo/:id', function(req, res) {
        Todos.findById({_id:req.params.id},
                   function(err, todo) {
                       if (err) throw err;

                       res.send(todo);
        });
    });

    app.post('/api/todo', function(req, res) {
        
        if (req.body.id) {
            Todos.findByIdAndUpdate(req.params.id, {
                todo: req.body.todo, isDone: req.body.isDone,
                hasAttachment: req.body.hasAttachment
                },
                function(err) {
                    if (err) throw err;
                    
                    res.send('updated:' + req.params.id);
                });
        }
        else {
            var newTodo = Todos({
                username: 'test',
                todo: req.body.todo,
                isDone: req.body.isDone,
                hasAttachment: req.body.hasAttachment
            });
            newTodo.save(function(err) {
                if (err) throw err;
                res.send('added');
            });
        }
    });

    app.delete('/api/delete/', function(req, res) {
        Todos.findByIdAndRemove(req.body.id, function(err) {
            if (err) throw err;

            res.send('deleted:'+ req.body.id);
        })
    })
}

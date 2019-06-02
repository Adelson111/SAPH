var express = require('express');
var router = express.Router();

router.get('/new',(req, res, next)=>{
  solicitacoes = [
    {
      'tipo':'tipo1',
      'itens':[
        {
          'nome':'s1item1',
          'campos':[
            {
              'nome':'campo1',
              'tipo':'text',
            },
            {
              'nome':'campo2',
              'tipo':'text',
            }
          ]
        },
        {
          'nome':'s1item2',
          'campos':[
            {
              'nome':'campo1',
              'tipo':'text',
            },
            {
              'nome':'campo2',
              'tipo':'file',
            },{
              'nome':'campo3',
              'tipo':'number',
            }
          ]
        },
      ],
    },
    {
      'tipo':'tipo2',
      'itens':[
        {
          'nome':'s2item1',
          'campos':[
            {
              'nome':'campo1',
              'tipo':'text',
            },
            {
              'nome':'campo3',
              'tipo':'number',
            }
          ]
        },
        {
          'nome':'s2item2',
          'campos':[
            {
              'nome':'campo3',
              'tipo':'number',
            }
          ]
        },
        {
          'nome':'s2item3',
          'campos':[
            {
              'nome':'campo1',
              'tipo':'text',
            },
            {
              'nome':'campo2',
              'tipo':'file',
            },
            {
              'nome':'campo3',
              'tipo':'number',
            },
            {
              'nome':'campo4',
              'tipo':'number',
            }
          ]
        },
      ],
    },
    {
      'tipo':'tipo3',
      'itens':[
        {
          'nome':'s3item1',
          'campos':[
            {
              'nome':'campo3',
              'tipo':'number',
            },
          ],
        },
      ],
    },
  ];
  res.render('new', {
    title: 'Solicitacoes - SAPH',
    tipos: solicitacoes,
  });
});
module.exports = router;
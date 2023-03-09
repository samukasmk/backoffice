from tasks import (membership,
                   messenger,
                   packing_slip,
                   royalties,
                   seller_commission)

registered_tasks = {'membership.subscription': membership.subscription,
                    'messenger.send_email': messenger.send_email,
                    'packing_slip.create_pdf_file': packing_slip.create_pdf_file,
                    'royalties.create_payment': royalties.create_payment,
                    'seller_commission.create_payment': seller_commission.create_payment}
